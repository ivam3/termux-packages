#!/data/data/com.termux/files/usr/bin/env node
// walkie patch: generic AI-agent runner for `walkie agent --cli <any>`
//
// Applied by postinst after install (same pattern as the netlink/SELinux
// patch). Idempotent: a marker comment is inserted on first run, and a
// subsequent run exits early. Each replacement is checked against its exact
// anchor string; if any anchor is missing the patch fails loudly so the
// postinst can abort instead of shipping a broken install.
//
// Features:
//   - Relaxes the --cli validation so any agent CLI can power `walkie agent`.
//   - Injects a generic runner (runGeneric) with a per-agent invocation
//     registry plus a native --skip-git-repo-check option for codex.
//   - Adds local AI support via Ollama (runOllama, HTTP API) — the daemon
//     only needs a local ollama server (default http://127.0.0.1:11434).
//
// Usage: node patch-agents.js <path-to-walkie.js>

const fs = require('fs')

const target = process.argv[2]
if (!target) {
  console.error('walkie-patch: missing walkie.js path argument')
  process.exit(1)
}

const MARKER = '/* walkie-patch-agents */'

const RUN_GENERIC = `function runGeneric(cli, prompt, sessionId, model, extraArgs) {
  const { spawnSync } = require('child_process')
  // Invocation registry: known agents and how to pass the prompt.
  // '{prompt}' is replaced inline with the message; if absent, the prompt is
  // appended as a positional argument (fallback for any unknown CLI).
  const REGISTRY = {
    agy: ['-p', '{prompt}'],
    vibe: ['-p', '{prompt}', '--output', 'text'],
    opencode: ['run', '{prompt}'],
    gemini: ['-p', '{prompt}'], qwen: ['-p', '{prompt}'], 'qwen-code': ['-p', '{prompt}'],
    mimo: ['-p', '{prompt}'], mimocode: ['-p', '{prompt}'],
    kilo: ['-p', '{prompt}'], kilocode: ['-p', '{prompt}'],
    minimax: ['-p', '{prompt}'], mmx: ['-p', '{prompt}'],
    'copilot-cli': ['{prompt}'], copilot: ['{prompt}'], codebuff: ['{prompt}'],
    freebuff: ['{prompt}'], hermes: ['{prompt}'], openclaw: ['{prompt}'],
    cactus: ['run', '--prompt', '{prompt}']
  }
  let args = (REGISTRY[cli] || ['{prompt}']).slice()
  if (model) {
    // cactus takes the model positionally: cactus run [model] (no --model).
    if (cli === 'cactus') args.push(model)
    else args.push('--model', model)
  }
  if (extraArgs) args.push(...extraArgs)
  if (args.includes('{prompt}')) {
    args = args.map(a => a === '{prompt}' ? prompt : a)
  } else {
    args.push(prompt)
  }

  // cactus writes a structured result to --result-json; prefer parsing the
  // clean response over the raw stdout, which also echoes the interactive
  // banner/You:/stats framing.
  let rjPath = null
  if (cli === 'cactus') {
    const os = require('os')
    const path = require('path')
    rjPath = path.join(os.tmpdir(), 'walkie-cactus-' + process.pid + '-' + Date.now() + '.json')
    args.push('--result-json', rjPath)
  }

  const result = spawnSync(cli, args, {
    timeout: 300000,
    maxBuffer: 10 * 1024 * 1024,
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe']
  })

  if (result.error) throw result.error
  if (result.status !== 0) throw new Error(result.stderr || cli + ' exited with code ' + result.status)

  let text = (result.stdout || '').trim()
  if (rjPath) {
    try {
      const rj = JSON.parse(require('fs').readFileSync(rjPath, 'utf8'))
      text = (rj.context_response || rj.response || text).trim()
    } catch {}
    try { require('fs').unlinkSync(rjPath) } catch {}
  }
  text = text.replace(/\\x1b\\[[0-9;]*[A-Za-z]/g, '')
  return { text, sessionId: null }
}

// Local LLM via the Ollama HTTP API (Node >= 18 has native fetch).
// Model resolution: --model > $OLLAMA_MODEL > first local model > fallback.
const ollamaHistory = []
async function runOllama(prompt, sessionId, model, extraArgs) {
  const base = (process.env.OLLAMA_HOST || 'http://127.0.0.1:11434').replace(/\\/+$/, '')
  let mdl = model || process.env.OLLAMA_MODEL || ''
  if (!mdl) {
    try {
      const tags = await fetch(base + '/api/tags', { signal: AbortSignal.timeout(5000) })
      if (tags.ok) {
        const data = await tags.json()
        const local = (data.models || []).filter(m => !m.name.includes(':cloud')).map(m => m.name)
        mdl = (local[0] || 'qwen2.5-coder:1.5b')
      }
    } catch {}
    mdl = mdl || 'qwen2.5-coder:1.5b'
  }

  ollamaHistory.push({ role: 'user', content: prompt })
  if (ollamaHistory.length > 40) ollamaHistory.splice(0, ollamaHistory.length - 40)

  let res
  try {
    res = await fetch(base + '/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: mdl, messages: ollamaHistory, stream: false }),
      signal: AbortSignal.timeout(300000)
    })
  } catch (e) {
    throw new Error('ollama server not running at ' + base + ' (' + e.message + ')')
  }
  if (!res.ok) {
    const body = await res.text().catch(() => '')
    throw new Error('ollama HTTP ' + res.status + ': ' + body.slice(0, 300))
  }
  const data = await res.json()
  const text = ((data.message && data.message.content) || '').trim()
  if (text) ollamaHistory.push({ role: 'assistant', content: text })
  return { text, sessionId: null }
}

`

const replacements = [
  {
    name: 'relax --cli validation',
    from: `    if (cli !== 'claude' && cli !== 'codex') {
      console.error(\`Error: unsupported CLI "\${cli}". Use "claude" or "codex".\`)
      process.exit(1)
    }`,
    to: `    ${MARKER}`
  },
  {
    name: 'inject runGeneric dispatcher',
    from: `program
  .command('agent <channel>')`,
    to: RUN_GENERIC + `program
  .command('agent <channel>')`
  },
  {
    name: 'register --skip-git-repo-check option',
    from: `  .option('--name <name>', 'Agent display name')
  .option('--agent-args <args>', 'Extra CLI arguments passed to claude/codex (e.g. "--dangerously-skip-permissions")')`,
    to: `  .option('--name <name>', 'Agent display name')
  .option('--agent-args <args>', 'Extra CLI arguments passed to claude/codex (e.g. "--dangerously-skip-permissions")')
  .option('--skip-git-repo-check', 'Skip the git repository check (only forwarded to agents that support it, e.g. codex)')`
  },
  {
    name: 'wire generic runner into askFn',
    from: `    const askFn = cli === 'claude' ? runClaude : runCodex`,
    to: `    const askFn = cli === 'claude' ? runClaude : (cli === 'codex' ? (p, s, m, a) => runCodex(p, s, m, [...(a || []), ...(opts.skipGitRepoCheck ? ['--skip-git-repo-check'] : [])]) : (cli === 'ollama' ? runOllama : (p, s, m, a) => runGeneric(cli, p, s, m, a)))`
  },
  {
    name: 'await async runners (ollama)',
    from: `          const out = askFn(prompt, sessionId, opts.model, extraArgs)`,
    to: `          const out = await askFn(prompt, sessionId, opts.model, extraArgs)`
  }
]

let src
try {
  src = fs.readFileSync(target, 'utf8')
} catch (e) {
  console.error('walkie-patch: cannot read ' + target + ': ' + e.message)
  process.exit(1)
}

if (src.includes(MARKER)) {
  console.log('walkie-patch: already applied, skipping')
  process.exit(0)
}

for (const r of replacements) {
  if (!src.includes(r.from)) {
    console.error('walkie-patch: FAILED to apply "' + r.name + '" — anchor not found in ' + target)
    process.exit(1)
  }
  src = src.split(r.from).join(r.to)
}

fs.writeFileSync(target, src)
console.log('walkie-patch: generic agent runner applied to ' + target)

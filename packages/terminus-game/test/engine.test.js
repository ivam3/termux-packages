'use strict';

const test = require('node:test');
const assert = require('node:assert');
const path = require('path');

const { TerminusEngine } = require('../lib/engine');

const ROOT = path.resolve(__dirname, '..');

function engine(cookie) {
  return new TerminusEngine({ root: ROOT, cookie: cookie || '' });
}

test('starts at Home with the expected exits', () => {
  const game = engine();
  assert.strictEqual(game.roomName(), 'Home');
  const result = game.command('ls');
  assert.match(result.output, /WesternForest/);
  assert.match(result.output, /NorthernMeadow/);
  assert.match(result.output, /MIT/);
  assert.match(result.output, /WelcomeLetter/);
});

test('cd moves the player and prints the intro text', () => {
  const game = engine();
  const result = game.command('cd WesternForest');
  assert.strictEqual(game.roomName(), 'WesternForest');
  assert.match(result.output, /You have moved to WesternForest/);
  assert.match(result.output, /Spell Casting Academy/);
});

test('less captures the item image', () => {
  const game = engine();
  game.command('cd WesternForest');
  const result = game.command('less Sign');
  assert.match(result.output, /Free Introductory Lessons/);
  assert.strictEqual(result.image, 'loc_forest.gif');
});

test('ls on a room path lists that room', () => {
  const game = engine();
  const result = game.command('ls WesternForest/SpellCastingAcademy');
  assert.match(result.output, /PracticeRoom/);
  assert.match(result.output, /Lessons/);
  assert.strictEqual(game.roomName(), 'Home');
});

test('unreachable paths are rejected without crashing', () => {
  const game = engine();
  const result = game.command('cd WesternForest/MIT');
  assert.match(result.output, /not reachable/);
  assert.strictEqual(game.roomName(), 'Home');
});

test('unknown commands report the room', () => {
  const game = engine();
  const result = game.command('tellme combo');
  assert.match(result.output, /Command 'tellme' not found in room 'Home'/);
});

test('man pages are available', () => {
  const game = engine();
  const result = game.command('man ls');
  assert.match(result.output, /Look at your Surroundings/);
});

test('pwd reports the current room', () => {
  const game = engine();
  game.command('cd WesternForest');
  const result = game.command('pwd');
  assert.match(result.output, /You are in WesternForest/);
});

test('state round-trips through the saved cookie', () => {
  const first = engine();
  first.command('cd WesternForest');
  first.command('cd SpellCastingAcademy');
  const state = first.stateString();
  assert.match(state, /^SpellCastingAcademy=/);

  const second = engine('terminuscookie=' + state);
  assert.strictEqual(second.roomName(), 'SpellCastingAcademy');
  assert.match(second.command('ls').output, /PracticeRoom/);
});

test('an unknown saved room falls back to Home', () => {
  const game = engine('terminuscookie=NoSuchRoom=broken:1=');
  assert.strictEqual(game.roomName(), 'Home');
  assert.match(game.command('ls').output, /WesternForest/);
});

test('replayed puzzle state links rooms and moves items', () => {
  const game = engine('terminuscookie=DankRoom=mvBoulder:1=');
  assert.strictEqual(game.roomName(), 'DankRoom');
  const children = game.room().children.map(String);
  assert.ok(children.includes('Tunnel'));
  const smallHole = game.sandbox.SmallHole.items.map(String);
  assert.ok(smallHole.includes('Boulder'));
});

test('exit requests the process to stop', () => {
  const game = engine();
  const result = game.command('exit');
  assert.strictEqual(result.exit, true);
});

function spanish(cookie) {
  return new TerminusEngine({ root: ROOT, cookie: cookie || '', lang: 'es' });
}

test('Spanish mode translates pwd, ls and man pages', () => {
  const game = spanish();
  assert.match(game.command('pwd').output, /Estás en Home/);
  const listed = game.command('ls').output;
  assert.match(listed, /Lugares:/);
  assert.match(listed, /Objetos:/);
  assert.match(game.command('man cd').output, /La voz del anciano/);
});

test('Spanish mode translates room intros and item descriptions', () => {
  const game = spanish();
  const moved = game.command('cd WesternForest');
  assert.match(moved.output, /Te has movido a WesternForest/);
  assert.match(moved.output, /Academia de Lanzamiento de Hechizos/);
  assert.match(game.command('less BackSign').output, /ir directamente a Home/);
});

test('Spanish mode keeps the English books and adds a note', () => {
  const game = spanish();
  game.sandbox.enterRoom(game.sandbox.MoreKernelFiles);
  const result = game.command('less L_txt');
  assert.match(result.output, /Texto original en inglés/);
  assert.match(result.output, /Alice was beginning/);
});

test('Spanish mode keeps the grep password line searchable', () => {
  const game = spanish();
  game.sandbox.enterRoom(game.sandbox.MoreKernelFiles);
  const result = game.command('grep password= U_txt');
  assert.match(result.output, /password=IHTFP/);
});

test('Spanish mode translates generated command feedback', () => {
  const game = spanish();
  assert.match(game.command('tellme combo').output, /Comando 'tellme' no encontrado/);
  game.sandbox.enterRoom(game.sandbox.Clearing);
  assert.match(game.command('less MissingThing').output, /No hay ningún MissingThing aquí/);
});

test('Spanish mode preserves the saved state', () => {
  const first = spanish();
  first.command('cd WesternForest');
  first.command('cd SpellCastingAcademy');
  const state = first.stateString();
  assert.match(state, /^SpellCastingAcademy=/);
  const second = spanish('terminuscookie=' + state);
  assert.strictEqual(second.roomName(), 'SpellCastingAcademy');
  assert.match(second.command('pwd').output, /Estás en SpellCastingAcademy/);
});

test('language flags default to English and accept Spanish', () => {
  const { parseArgs } = require('../lib/cli');
  assert.strictEqual(parseArgs([]).lang, 'en');
  assert.strictEqual(parseArgs(['--esp']).lang, 'es');
  assert.strictEqual(parseArgs(['--lang', 'es']).lang, 'es');
  assert.strictEqual(parseArgs(['--lang=en']).lang, 'en');
  assert.strictEqual(parseArgs([], 'es').lang, 'es');
  assert.throws(() => parseArgs(['--lang', 'fr']), /invalid language/);
});

test('Spanish mode translates the Instructions item', () => {
  const game = spanish();
  game.sandbox.enterRoom(game.sandbox.KernelFiles);
  const result = game.command('less Instructions');
  assert.match(result.output, /Veo que has aprendido a usar a tu amigo grep/);
  assert.doesNotMatch(result.output, /Texto original en inglés/);
});

test('Spanish mode translates dynamic text replayed from a save', () => {
  const game = spanish('terminuscookie=DankRoom=mvBoulder:1=');
  assert.strictEqual(game.roomName(), 'DankRoom');
  assert.match(game.sandbox.Tunnel.intro_text, /Aquí dentro hay bastante humedad/);
  assert.match(game.command('ls').output, /Lugares:/);
});

test('BrokenBridge remains case-sensitive', () => {
  const game = engine('terminuscookie=BrokenBridge=');
  const lower = game.command('touch plank');
  assert.match(lower.output, /created plank/);
  assert.match(game.command('cd Clearing').output, /can’t cross the bridge/);
  assert.strictEqual(game.roomName(), 'BrokenBridge');

  const upper = game.command('touch Plank');
  assert.match(upper.output, /created Plank/);
  assert.match(game.command('cd Clearing').output, /You have moved to Clearing/);
  assert.strictEqual(game.roomName(), 'Clearing');
});

test('rescues the kidnapped child and persists the state', () => {
  const game = engine('terminuscookie=CaveOfDisgruntledTrolls=');
  const result = game.command('mv KidnappedChild');
  assert.match(result.output, /dashes past you/);
  assert.strictEqual(game.sandbox.Cage.items.length, 0);
  assert.ok(game.sandbox.Clearing.items.map(String).includes('KidnappedChild'));
  assert.match(game.stateString(), /freeKid:1/);

  const resumed = engine('terminuscookie=' + game.stateString());
  assert.strictEqual(resumed.sandbox.Cage.items.length, 0);
  assert.ok(resumed.sandbox.Clearing.items.map(String).includes('KidnappedChild'));
  assert.match(resumed.command('mv KidnappedChild').output, /already free/);
});

test('Spanish mode translates the child rescue and already-free message', () => {
  const game = spanish('terminuscookie=CaveOfDisgruntledTrolls=');
  const result = game.command('mv KidnappedChild');
  assert.match(result.output, /niña/);
  assert.match(result.output, /sendero inquietante/);
  assert.match(game.command('mv KidnappedChild').output, /La niña ya está libre/);
});

test('walkthrough reaches Paradise', () => {
  const game = engine();
  const commands = [
    'cd NorthernMeadow',
    'cd EasternMountains',
    'cd Cave',
    'cd DarkCorridor',
    'cd DankRoom',
    'mv Boulder SmallHole',
    'cd Tunnel',
    'cd StoneChamber',
    'cd Portal',
    'cd TownSquare',
    'cd BrokenBridge',
    'touch Plank',
    'cd Clearing',
    'cd OminousLookingPath',
    'rm ThornyBrambles',
    'cd CaveOfDisgruntledTrolls',
    'rm UglyTroll',
    'cd Slide',
    'cd KernelFiles',
    'cd MoreKernelFiles',
    'grep password= U_txt',
    'cd ..',
    'sudo less Certificate',
    'IHTFP'
  ];
  let result = null;
  for (const command of commands) {
    result = game.command(command);
  }
  assert.strictEqual(game.roomName(), 'Paradise');
  assert.match(result.output, /congratulations/);
  assert.match(game.stateString(), /sudoComplete:1/);
});

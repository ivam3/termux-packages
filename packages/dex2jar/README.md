# dex2jar

> Tools to work with android .dex and java .class files.

## Installation

```bash
pkg install dex2jar
```

## Info

| Field | Value |
|-------|-------|
| Version | `2.4` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [dex2jar](https://github.com/pxb1988/dex2jar) |

## Dependencies

`curl, unzip, openjdk-21`

## Usage

```bash
dex2jar                      # list available tools
dex2jar <tool> <options + arguments>
```

> Example: `dex2jar d2j-dex2jar -f ~/path/to/apk_to_decompile.apk` converts a DEX file to JAR.
>
> The tool scripts are downloaded to `~/.local/share/dex2jar` on install and are executed with `openjdk-21`.

## Suggestions

Also install: `fixer`
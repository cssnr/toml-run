---
icon: lucide/notebook-pen
---

# :lucide-notebook-pen: Reference

[![TOML Run](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)

- [Install](#install)
- [Scripts](#scripts)
- [Usage](#usage)
- [Environment](#environment)

The CLI executable is `run` or `toml-run` and help is available with `--help`.

```shell
usage: run [-l] [-c CONFIG] [-s] [-v] [-V] [-D] [-h] [name]  # (1)!

example: run [name] -- --script-args

positional arguments:
  name                 Name of script to run

options:
  -l, --list           List available scripts
  -c, --config CONFIG  Config [default: pyproject.toml]
  -s, --silent         Disable script output
  -v, --verbose        Verbose output [debug: -vvv]
  -V, --version        Show installed version
  -D, --docs           Launch docs in browser
  -h, --help           Show this help message
```

1. :lucide-lightbulb: Tip: Save your options with [Environment Variables](#environment).

To view the source code, see the [cli.py :lucide-arrow-up-right:](https://github.com/cssnr/toml-run/blob/master/src/tomlrun/cli.py) on GitHub.

## :simple-pypi: Install

From PyPI: <https://pypi.org/p/toml-run>  
GitHub: [https://github.com/cssnr/toml-run](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)

=== "uv"

    ```shell
    uv tool install toml-run
    ```

=== "uv-dev"

    ```shell
    uv add --dev toml-run
    ```

=== "pip"

    ```shell
    pip install toml-run
    ```

=== "pip-dev"

    ```shell
    pip install --group dev toml-run
    ```

=== "brew"

    ```shell
    brew install cssnr/tap/toml-run
    ```

Upgrade.

=== "uv"

    ```shell
    uv tool upgrade toml-run
    ```

=== "uv-dev"

    ```shell
    uv sync --upgrade-package toml-run
    ```

=== "pip"

    ```shell
    pip install -U toml-run
    ```

=== "pip-dev"

    ```shell
    pip install -U toml-run
    ```

=== "brew"

    ```shell
    brew update && brew install toml-run
    ```

Uninstall.

=== "uv"

    ```shell
    uv tool uninstall toml-run
    ```

=== "uv-dev"

    ```shell
    uv remove --group dev toml-run
    ```

=== "pip"

    ```shell
    pip uninstall toml-run
    ```

=== "pip-dev"

    ```shell
    pip uninstall toml-run
    ```

=== "brew"

    ```shell
    brew uninstall toml-run
    ```

Run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx toml-run
```

Check the installed `--version`.

```shell
run -V
```

## :simple-toml: Scripts

Scripts are defined in the `pyproject.toml` using the `[tool.scripts]` section.

```toml title="pyproject.toml"
[tool.scripts]  # (1)!
build = "uv run hatch build"
```

1. Supported headings: `[tool.scripts]` and `[tool.toml-run]`

Define "pre" and "post" scripts by prefixing the script name.

```toml
prebuild = "echo always run before build"
build = "echo running build"
postbuild = "echo always run after build"
```

Split commands into multiple commands.

```toml
as-list = ["echo one", "echo two"]
as_string = """
echo one
echo two
"""
```

Chain commands and run other commands.

```toml
one = "echo one"
two = "run one && echo two"
success = "run one && echo success || echo failed"
failure = "run abc && echo success || echo failed"
```

All paths are relative to the config file directory.

```toml title="pyproject.toml"
clean = "rm -rf dist"
```

Therefore, `clean` will always remove this `dist` folder.

```text
.
├── pyproject.toml
└── dist
```

Run Python code using `eval` easily. :lucide-flask-conical:{ title="Experimental Feature!" }

```toml
unlink = "#py Path('file').unlink(True)"
rmtree = "#py shutil.rmtree('dir', True)"
web = "#py webbrowser.open_new_tab('https://github.com/cssnr/toml-run')"
chain = ["run rmtree", "#py print('two')", "echo three", "run web"]
```

You can use these in a list and with run just not using `&&`.
The only parsing done is looking for `#py` at the start of a string and running eval.
You can view the list of imported modules below.

??? details "Imported Modules"

    ```python
    import os
    import shutil
    import subprocess
    import sys
    import webbrowser
    from pathlib import Path
    from pprint import pformat
    ```

## :lucide-square-terminal: Usage

The CLI executable is `run` or `toml-run`.

List available scripts with `--list`.

```shell
run -l
```

Run a script with `run`.

```shell
run build
```

Run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx toml-run build
```

Pass additional arguments after `--` terminator.

```shell
run build -- --clean
```

Increase output with `--verbose`. Debug with `-vv` or `-vvv`.

```shell
run build -v
```

Silent script output with `--silent`.

```shell
run build -s
```

If your scripts are defined in another file use `--config`.

```shell
run -c settings.toml build
```

This will look for a `settings.toml` in current and parent directories and run the scripts relative to that files directory.

You can set the `SCRIPT_CONFIG` [Environment](#environment) variable to avoid using the `--config` option every time.

## :lucide-list: Environment

Many options support setting environment variable defaults.

| Environment&nbsp;Variable |    Default     |  Type  | Description           |
| :------------------------ | :------------: | :----: | :-------------------- |
| `SCRIPT_SILENT`           |     false      | `bool` | Disable script output |
| `SCRIPT_VERBOSE`          |       0        | `int`  | Enable verbose output |
| `SCRIPT_CONFIG`           | pyproject.toml | `str`  | Python Project File   |

Allowed boolean values, case-insensitive.

```plain
0, f, n, no, off, false
1, t, y, on, yes, true
```

You can temporarily set variables on the command line.

=== "Unix"

    ```shell
    export SCRIPT_VERBOSE=1
    ```

=== "Windows"

    ```pwsh
    $env:SCRIPT_VERBOSE=1
    ```

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!

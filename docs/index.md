---
icon: lucide/rocket
---

# :lucide-rocket: Get Started

[![TOML Run](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)

[![PyPI Version](https://img.shields.io/pypi/v/toml-run?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/toml-run/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Ftoml-run%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/toml-run?logo=pypi&logoColor=white)](https://pypistats.org/packages/toml-run)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/toml-run?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/toml-run)
[![Codecov](https://codecov.io/gh/cssnr/toml-run/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/toml-run)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/toml-run/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/toml-run/actions/workflows/test.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/toml-run?logo=github&label=updated)](https://github.com/cssnr/toml-run/pulse)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/toml-run?style=flat&logo=github)](https://github.com/cssnr/toml-run/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/toml-run?style=flat&logo=github)](https://github.com/cssnr/toml-run/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Define custom scripts in your pyproject.toml and easily run them with this dependency free tool.
This tool is both inspired by and similar to [NPM Scripts :lucide-arrow-up-right:](https://docs.npmjs.com/cli/v8/using-npm/scripts).

To get started see the [Quick Start](#quick-start) section or check out the [Features](#features).

=== "uv"

    ```shell
    uv tool install toml-run
    ```

=== "uv + dev"

    ```shell
    uv add --dev toml-run
    ```

=== "pip"

    ```shell
    pip install toml-run
    ```

=== "pip + dev"

    ```shell
    pip install --group dev toml-run
    ```

=== "brew"

    ```shell
    brew tap cssnr/tap
    brew install toml-run
    ```

```toml title="pyproject.toml"
[tool.scripts]
build = "uv run hatch build"
```

```shell
run build
```

!!! tip "There are detailed [Install](reference.md#install), [Script](reference.md#scripts) and [Usage](reference.md#usage) guides available."

If you run into any issues or have any questions, [support](support.md) is available.

## :lucide-sparkles: Features

- Define scripts in your `pyproject.toml`
- Easily run scripts with `run [name]`
- Cross-platform support using subprocess
- Supports `pre` and `post` scripts
- Supports multiple commands per script
- Pass additional arguments to scripts
- Automatically finds the `pyproject.toml`
- Runs scripts relative to the root directory
- Evaluate python code :lucide-flask-conical:{ title="Experimental Feature!" }

For more details see the [full reference](reference.md).

## :lucide-plane-takeoff: Quick Start

First, [install](reference.md#install) the package from [PyPi :lucide-arrow-up-right:](https://pypi.org/p/toml-run)
or [GitHub :lucide-arrow-up-right:](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme).

=== "uv"

    ```shell
    uv tool install toml-run
    ```

=== "uv + dev"

    ```shell
    uv add --dev toml-run
    ```

=== "pip"

    ```shell
    pip install toml-run
    ```

=== "pip + dev"

    ```shell
    pip install --group dev toml-run
    ```

=== "brew"

    ```shell
    brew tap cssnr/tap
    brew install toml-run
    ```

Then, add some [scripts](reference.md#scripts) to the `pyproject.toml`.

```toml title="pyproject.toml"
[tool.scripts]
clean = "rm -rf dist"
build = "run clean && uv run hatch build"
prelint = "echo always runs before lint"
lint = ["uv run ruff check .", "uv run ty check ."]
postlint = "echo always runs after lint"
```

Finally, [run](reference.md#usage) a script.

```shell
run build
```

Or, run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx toml-run build
```

[:simple-toml: Script Reference](reference.md#scripts){ .md-button .md-button--primary }

[:lucide-square-terminal: Usage Reference](reference.md#usage){ .md-button .md-button--primary }

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!

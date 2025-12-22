[![PyPI Version](https://img.shields.io/pypi/v/toml-run?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/toml-run/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/releases)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Ftoml-run%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/toml-run?logo=pypi&logoColor=white)](https://pypistats.org/packages/toml-run)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/toml-run?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/toml-run)
[![Codecov](https://codecov.io/gh/cssnr/toml-run/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/toml-run)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/toml-run/lint.yaml?logo=cachet&label=lint)](https://github.com/cssnr/toml-run/actions/workflows/lint.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/toml-run/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/toml-run/actions/workflows/test.yaml)
[![Deployment PyPi](https://img.shields.io/github/deployments/cssnr/toml-run/pypi?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/toml-run/)
[![Deployment Docs](https://img.shields.io/github/deployments/cssnr/toml-run/docs?logo=materialformkdocs&logoColor=white&label=docs)](https://cssnr.github.io/toml-run/)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/toml-run?logo=github&label=updated)](https://github.com/cssnr/toml-run/pulse)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/toml-run?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/toml-run)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/toml-run?logo=htmx&logoColor=white)](https://github.com/cssnr/toml-run?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/toml-run?logo=github)](https://github.com/cssnr/toml-run/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/toml-run?style=flat&logo=github)](https://github.com/cssnr/toml-run/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/toml-run?style=flat&logo=github)](https://github.com/cssnr/toml-run/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# TOML Run

<a title="TOML Run" href="https://cssnr.github.io/toml-run/" target="_blank">
<img alt="TOML Run" align="right" width="128" height="auto" src="https://cssnr.github.io/toml-run/assets/images/logo.svg"></a>

- [Features](#features)
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

Define custom scripts in your pyproject.toml and easily run them with this dependency free tool.
This tool is both inspired by and similar to [NPM Scripts](https://docs.npmjs.com/cli/v8/using-npm/scripts).

If you run into any issues or have any questions, [support](#support) is available.

To get started [Install](#install) the cli and view the [Usage](#usage).

[![View Documentation](https://img.shields.io/badge/view_documentation-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/toml-run/)

## Features<a id="features"></a>

- Define scripts in your `pyproject.toml`
- Easily run scripts with `run [name]`
- Cross-platform support using subprocess
- Supports `pre` and `post` scripts
- Supports multiple commands per script
- Pass additional arguments to scripts
- Automatically finds the `pyproject.toml`
- Runs scripts relative to the root directory
- Evaluate python code 🧪 _(experimental)_

[![View Full Reference](https://img.shields.io/badge/view_full_reference-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/toml-run/reference/)

## Install<a id="install"></a>

From PyPI: <https://pypi.org/p/toml-run>

```shell
pip install toml-run
pip install --group dev toml-run

uv tool install toml-run
uv add --dev toml-run
```

[![View Install Guide](https://img.shields.io/badge/view_install_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/toml-run/reference/#install)

## Usage<a id="usage"></a>

First, add some scripts to the `pyproject.toml` using the `[tool.scripts]` section.

```toml title="pyproject.toml"
[tool.scripts]
prepare = "python scripts/prepare.py"
build = "run prepare && uv run hatch build"
prelint = "echo always runs before lint"
lint = ["black --check .", "ruff check ."]
postlint = "echo always runs after lint"
format = """
black .
ruff format .
"""
clean = "#py shutil.rmtree('.cache', True)"
```

[![View Scripts Guide](https://img.shields.io/badge/view_scripts_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/toml-run/reference/#scripts)

Run scripts with the `run` command.

```shell
run build
```

List available scripts with `--list`.

```shell
run -l
```

Run without installing using [astral-sh/uv](https://docs.astral.sh/uv/).

```shell
uvx toml-run build
```

[![View Usage Guide](https://img.shields.io/badge/view_usage_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/toml-run/reference/#usage)

## Support<a id="support"></a>

If you run into any issues or need help getting started, please do one of the following:

- Report an Issue: <https://github.com/cssnr/toml-run/issues>
- Q&A Discussion: <https://github.com/cssnr/toml-run/discussions/categories/q-a>
- Request a Feature: <https://github.com/cssnr/toml-run/issues/new?template=1-feature.yaml>
- Chat with us on Discord: <https://discord.gg/wXy6m2X8wY>

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://github.com/cssnr/toml-run/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/toml-run/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=rocketdotchat&logoColor=white)](https://github.com/cssnr/toml-run/discussions)
[![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

## Contributing<a id="contributing"></a>

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)

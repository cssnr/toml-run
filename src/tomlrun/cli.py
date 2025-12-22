import argparse
import os
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from pprint import pformat
from typing import Any, Dict, List, Optional

from . import utils
from ._version import __version__


try:
    from tomllib import load  # type: ignore
except ImportError:  # pragma: no cover
    from tomli import load  # type: ignore


docs = "https://cssnr.github.io/toml-run/"
state = {"silent": False, "verbose": 0}

Scripts = Dict[str, List[str]]


class DocsAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        result = webbrowser.open_new_tab(docs)
        if not result:
            raise ValueError(f"Unable to launch browser.\n\nVisit: {docs}\n")
        sys.exit(0)


def vprint(*objects: Any, lvl=1, sep="\n", **kwargs):
    if state["verbose"] >= lvl:
        print(*objects, file=sys.stderr, sep=sep, **kwargs)


def print_rule(title: str, rule: str = "-", pre: int = 3):
    if state["verbose"]:
        # width = os.get_terminal_size().columns - 1
        width = shutil.get_terminal_size(fallback=(80, 24)).columns - 1
        text = f"{rule * pre} {title} "
        result = text + rule * (width - len(text))
        print(result[:width])


def get_config(path: Path) -> Optional[Path]:
    if path.is_file():
        return path
    if len(path.parts) == 1:
        cwd = Path.cwd()
        for directory in [cwd, *cwd.parents]:
            file = directory / str(path)
            if file.is_file():
                return file
    return None


def get_scripts(document: Dict[str, dict]) -> Optional[Scripts]:
    tool: Dict[str, dict] = document.get("tool", {})
    vprint(f"{tool=}\n", lvl=3)
    scripts = {}
    for key in ["toml-run", "scripts"]:
        if key in tool:
            scripts = tool[key]
            break
    if not scripts:
        return None
    vprint(f"{scripts=}\n", lvl=3)
    result: Scripts = {}
    for name, script in scripts.items():
        cmds = script if isinstance(script, list) else [script]
        result[name] = []
        for cmd in cmds:
            result[name].extend(cmd.strip().split("\n"))
    return result


def list_scripts(scripts: Scripts, pyproject: Path):
    print(f"\nConfig: {pyproject.absolute()}")
    print(f"Working Directory: {pyproject.parent.absolute()}")
    print(f"Scripts Found: {len(scripts)}\n")
    for name, script in scripts.items():
        cmds = " && ".join(script)
        print(f" - {name} :: {cmds}")
    print("")


def run_script(scripts: Scripts, name: str, path: Path, args: List[str]):
    vprint(f"Working Directory: {path.absolute()}")
    vprint(f"{args=}", lvl=2)
    os.chdir(path)  # for eval so it only happens once
    for prefix in ["pre", "", "post"]:
        script_name = f"{prefix}{name}"
        if commands := scripts.get(script_name):
            last = len(commands) - 1
            for i, command in enumerate(commands):
                # vprint(f"{prefix=}", f"{i=}", f"{last=}", f"{command=}")
                if command.startswith("#py"):
                    print_rule(f"{script_name} --- {command}", "-")
                    eval(command[3:])
                    continue
                if not prefix and args and i == last:
                    command = command + " " + " ".join(args)
                print_rule(f"{script_name} --- {command}", "-")
                subprocess.run(command, capture_output=bool(state["silent"]), check=True, shell=True, cwd=path)


def env(name: str) -> Any:
    result = os.environ.get(f"SCRIPT_{name}".upper())
    if name == "config":
        return Path(result or "pyproject.toml")
    if name == "silent":
        return utils.str_to_bool(result)
    if name == "verbose":
        return int(result) if result and result.isdigit() else 0


def run() -> None:
    parser = argparse.ArgumentParser(
        description="example: %(prog)s [name] -- --script-args", epilog=f"docs: {docs}", add_help=False
    )
    parser.add_argument("name", type=str, nargs="?", help="Name of script to run")
    parser.add_argument("-l", "--list", action="store_true", help="List available scripts")
    parser.add_argument("-c", "--config", type=Path, default=env("config"), help="Config [default: pyproject.toml]")
    parser.add_argument("-s", "--silent", action="store_true", default=env("silent"), help="Disable script output")
    parser.add_argument("-v", "--verbose", action="count", default=env("verbose"), help="Verbose output [debug: -vvv]")
    parser.add_argument("-V", "--version", action="version", version=__version__, help="Show installed version")
    parser.add_argument("-D", "--docs", action=DocsAction, nargs=0, help="Launch docs in browser")
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message")
    # parser.add_argument("args", nargs=argparse.REMAINDER, default=[])
    # args = parser.parse_args()
    args, remaining = parser.parse_known_args()
    # print(f"{args=}", f"{remaining=}", sep='\n')
    state["silent"] = args.silent
    state["verbose"] = args.verbose
    vprint(f"{state=}")
    vprint(f"{args=}", f"{remaining=}", lvl=2)

    config = get_config(args.config)
    if not config:
        raise ValueError(f"Config not found: {args.config}")

    vprint(f"Config: {config.absolute()}")
    with open(config, "rb") as f:
        document = load(f)
    vprint(f"{document=}\n", lvl=3)

    scripts: Optional[Scripts] = get_scripts(document)
    vprint(pformat(scripts), end="\n\n", lvl=3)
    if not scripts:
        raise ValueError(f"No scripts found in: {config.absolute()}")

    if args.list:
        list_scripts(scripts, config)
        raise SystemExit

    # name = getattr(args, "name", None)
    vprint(f"{args.name=}", lvl=2)
    if not args.name:
        if scripts:
            list_scripts(scripts, config)
        else:
            parser.print_help(sys.stderr)
        raise ValueError("No script name provided.")

    script: Optional[list] = scripts.get(args.name)
    vprint(f"{script=}", lvl=2)
    if not script:
        list_scripts(scripts, config)
        raise ValueError(f"Script not found: {args.name}")

    run_script(scripts, args.name, config.parent, remaining)


def main() -> None:
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(1)  # pragma: no cover
    except Exception as error:
        print(f"\nError: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()  # pragma: no cover

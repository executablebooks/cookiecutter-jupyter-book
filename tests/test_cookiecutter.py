import json
import subprocess
from pathlib import Path
from itertools import product
from pytest import fixture, mark

IGNORE = [".DS_Store", "__pycache__"]


@fixture()
def base_command(tmpdir):
    return (f"cookiecutter . --no-input --output-dir {tmpdir}", tmpdir)


def num_items(path, directory=[""]):
    files = [
        file for file in path.joinpath(*directory).iterdir() if file.name not in IGNORE
    ]
    return len(files)


def test_cookiecutter_default_options(base_command):
    result = subprocess.run(base_command[0], shell=True)
    assert result.returncode == 0


with open("cookiecutter.json") as f:
    options = json.load(f)
combinations = list(product(options["open_source_license"], options["include_ci"]))


@mark.parametrize("open_source_license,include_ci", combinations)
def test_cookiecutter_all_options(base_command, open_source_license, include_ci):
    params = f" open_source_license='{open_source_license}' include_ci={include_ci}"
    path = Path(base_command[1])
    result = subprocess.run(base_command[0] + params, shell=True)
    assert result.returncode == 0
    assert num_items(path, ["my_book", "my_book"]) == 9
    if open_source_license == "None":
        if include_ci == "github":
            assert num_items(path, ["my_book", ".github", "workflows"]) == 1
            assert num_items(path, ["my_book"]) == 6
        elif include_ci == "gitlab":
            assert num_items(path, ["my_book"]) == 6
        else:
            assert num_items(path, ["my_book"]) == 5
    else:
        if include_ci == "github":
            assert num_items(path, ["my_book", ".github", "workflows"]) == 1
            assert num_items(path, ["my_book"]) == 7
        elif include_ci == "gitlab":
            assert num_items(path, ["my_book"]) == 7
        else:
            assert num_items(path, ["my_book"]) == 6


def test_jupyter_book_cookiecutter(base_command):
    # same tests being run in the Jupyter Book test regime
    # https://github.com/executablebooks/jupyter-book/blob/main/tests/test_build.py#L26-L35
    # default cookiecutter book name is "my_book"
    path = Path(base_command[1])
    result = subprocess.run(base_command[0], shell=True)
    assert result.returncode == 0
    assert path.joinpath("my_book", "my_book", "_config.yml").exists()
    assert num_items(path, ["my_book"]) == 7
    assert num_items(path, ["my_book", ".github", "workflows"]) == 1
    assert num_items(path, ["my_book", "my_book"]) == 9


@mark.parametrize(
    "username,service,msg",
    [
        ("fake_captainjupyter_fake", "github", "WARNING"),
        ("fake_captainjupyter_fake", "gitlab", "WARNING"),
    ],
)
def test_warning_message(base_command, username, service, msg):
    result = subprocess.run(
        base_command[0] + f" include_ci={service}",
        shell=True,
        capture_output=True,
    )
    assert result.returncode == 0
    assert msg in result.stdout.decode("ascii")

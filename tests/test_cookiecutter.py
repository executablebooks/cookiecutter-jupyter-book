import json
import subprocess
from pathlib import Path
from itertools import product
from pytest import fixture, mark


@fixture()
def base_command(tmpdir):
    return (f"cookiecutter . --no-input --output-dir {tmpdir}", tmpdir)


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
    try:
        # annoying work-around for MAC OS .DS_Store files
        path.joinpath("my_book", ".DS_Store").unlink()
        path.joinpath("my_book", "my_book", ".DS_Store").unlink()
    except:
        pass
    assert len(list(path.joinpath("my_book", "my_book").iterdir())) == 8
    print(open_source_license)
    print(include_ci)
    if open_source_license == "None":
        if include_ci == "github":
            assert (
                len(list(path.joinpath("my_book", ".github", "workflows").iterdir()))
                == 1
            )
            assert len(list(path.joinpath("my_book").iterdir())) == 6
        elif include_ci == "gitlab":
            assert len(list(path.joinpath("my_book").iterdir())) == 6
        else:
            assert len(list(path.joinpath("my_book").iterdir())) == 5
    else:
        if include_ci == "github":
            assert (
                len(list(path.joinpath("my_book", ".github", "workflows").iterdir()))
                == 1
            )
            assert len(list(path.joinpath("my_book").iterdir())) == 7
        elif include_ci == "gitlab":
            assert len(list(path.joinpath("my_book").iterdir())) == 7
        else:
            assert len(list(path.joinpath("my_book").iterdir())) == 6


def test_jupyter_book_cookiecutter(base_command):
    # same tests being run in the Jupyter Book test regime
    # https://github.com/executablebooks/jupyter-book/blob/master/tests/test_build.py#L26-L35
    # note that default cookiecutter book name is "my_book" which is why it's used below
    path = Path(base_command[1])
    result = subprocess.run(base_command[0], shell=True)
    try:
        # annoying work-around for MAC OS .DS_Store files
        path.joinpath("my_book", ".DS_Store").unlink()
        path.joinpath("my_book", "my_book", ".DS_Store").unlink()
    except:
        pass
    assert result.returncode == 0
    assert path.joinpath("my_book", "my_book", "_config.yml").exists()
    print(list(path.joinpath("my_book").iterdir()))
    assert len(list(path.joinpath("my_book").iterdir())) == 7
    assert len(list(path.joinpath("my_book", ".github", "workflows").iterdir())) == 1
    assert len(list(path.joinpath("my_book", "my_book").iterdir())) == 8


@mark.parametrize(
    "username,service,msg",
    [
        ("fake_captainjupyter_fake", "github", "WARNING"),
        ("fake_captainjupyter_fake", "gitlab", "WARNING"),
    ],
)
def test_warning_message(base_command, username, service, msg):
    path = Path(base_command[1])
    result = subprocess.run(
        base_command[0] + f" include_ci={service}", shell=True, capture_output=True
    )
    print(result.stdout.decode("ascii"))
    assert result.returncode == 0
    assert msg in result.stdout.decode("ascii")

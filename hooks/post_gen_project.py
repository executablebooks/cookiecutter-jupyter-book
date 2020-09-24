# This script cleans up github workflows post CC generation
import os
import shutil
import requests
from textwrap import dedent

##############################################################################
# Path utilities


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


##############################################################################
# CLI utilities

border = "=" * 79
endc = "\033[0m"
bcolors = dict(
    blue="\033[94m",
    green="\033[92m",
    orange="\033[93m",
    red="\033[91m",
    bold="\033[1m",
    underline="\033[4m",
)


def _color_message(msg, style):
    return bcolors[style] + msg + endc


def _message_box(msg, color="green", doprint=True, print_func=print):
    # Prepare the message so the indentation is the same as the box
    msg = dedent(msg)

    # Color and create the box
    border_colored = _color_message(border, color)
    box = """
    {border_colored}
    {msg}
    {border_colored}
    """
    box = dedent(box).format(msg=msg, border_colored=border_colored)
    if doprint is True:
        print_func(box)
    return box


##############################################################################
# Post-gen script

github = "{{cookiecutter.include_ci}}" == "github"
gitlab = "{{cookiecutter.include_ci}}" == "gitlab"


if github:
    remove(".gitlab-ci.yml")
elif gitlab:
    remove(".github/")
else:
    # remove all CI
    remove(".github/")
    remove(".gitlab-ci.yml")


if (
    not requests.get(
        "http://www.github.com/{{cookiecutter.github_username}}"
    ).status_code
    < 400
):
    _message_box(
        "WARNING:\n"
        "Could not find the user '{{cookiecutter.github_username}}' on github.com.\n"
        "Please check the 'github_username' you entered.\n"
        "If you are not using github.com you may ignore this warning.",
        color="orange",
    )

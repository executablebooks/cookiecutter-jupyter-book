# This script cleans up github workflows post CC generation
import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


no_workflow = "{{cookiecutter.include_github_actions}}" == "no"

if no_workflow:
    # remove top-level file inside the generated folder
    remove(".github/")


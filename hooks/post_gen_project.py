#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    os.system("git init")
    os.system("git add *")
    os.system(
        "git add "
        f"{PROJECT_DIRECTORY}/.flake8 "
        f"{PROJECT_DIRECTORY}/.gitignore "
        f"{PROJECT_DIRECTORY}/.isort.cfg "
        f"{PROJECT_DIRECTORY}/.pre-commit-config.yaml "
    )
    os.system("pre-commit install")


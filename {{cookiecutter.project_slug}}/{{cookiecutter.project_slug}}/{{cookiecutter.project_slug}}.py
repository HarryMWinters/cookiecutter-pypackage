"""Main module."""


def hello_{{ cookiecutter.project_slug }}() -> str:
    """
    Quite the F401 demons from unused imports
    in the cli.
    """
    return "foo"
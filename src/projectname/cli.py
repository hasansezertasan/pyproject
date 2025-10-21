"""projectname CLI application."""
# mypy: disable-error-code="misc"

from __future__ import annotations

import platform
from importlib.metadata import Distribution

import typer

from projectname.config import PROJECT_NAME
from projectname.logging_setup import logger

app = typer.Typer(
    name="projectname",
    no_args_is_help=True,
)


@app.command(name="version")
def show_version() -> None:
    """Show the current version number of projectname.

    Show the version number:
        projectname version

    Example output:
        0.1.0
    """
    distribution = Distribution.from_name(PROJECT_NAME)
    logger.info("Command `version` called.")
    typer.echo(distribution.version)
    logger.info("Version displayed successfully.")


@app.command()
def info() -> None:
    """Display information about the projectname application.

    Show application information:
        projectname info

    Example output:
        Application Version: 0.1.0
        Python Version: 3.8.20 (CPython)
        Platform: Darwin
    """
    distribution = Distribution.from_name(PROJECT_NAME)
    logger.info("Command `info` called.")
    python_version = platform.python_version()
    python_implementation = platform.python_implementation()
    typer.echo(f"Application Version: {distribution.version}")
    typer.echo(f"Python Version: {python_version} ({python_implementation})")
    typer.echo(f"Platform: {platform.system()}")
    logger.info("Application information displayed successfully.")

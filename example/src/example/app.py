"""Web application."""
# mypy: disable-error-code="misc"

from __future__ import annotations

import platform
from importlib.metadata import Distribution

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

from example.config import PROJECT_NAME
from example.logging_setup import logger

app = FastAPI(title="example")


@app.get("/version", response_class=PlainTextResponse)
def get_version() -> str:
    """Return the current version number of example.

    Example response body:
        0.1.0
    """
    distribution = Distribution.from_name(PROJECT_NAME)
    logger.info("HTTP GET `/version` called.")
    logger.info("Version displayed successfully.")
    return distribution.version


@app.get("/info")
def get_info() -> JSONResponse:
    """Return basic runtime information about the application."""
    distribution = Distribution.from_name(PROJECT_NAME)
    logger.info("HTTP GET `/info` called.")
    python_version = platform.python_version()
    python_implementation = platform.python_implementation()
    payload = {
        "application_version": distribution.version,
        "python_version": python_version,
        "python_implementation": python_implementation,
        "platform": platform.system(),
    }
    logger.info("Application information displayed successfully.")
    return JSONResponse(content=payload)

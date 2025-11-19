from __future__ import annotations
from importlib.metadata import version, PackageNotFoundError
import logging

"""
my_package package initializer.

Provides:
- runtime version discovery via get_version()
- lightweight logger factory setup_logger() and a module logger
"""


__all__ = ["__version__", "get_version", "setup_logger", "logger"]

# __version__ will be resolved on demand by get_version()
__version__: str | None = None

def get_version() -> str:
    """Return the package version or '0.0.0' if not installed as a distribution."""
    global __version__
    if __version__:
        return __version__

    try:
        pass
    except Exception:
        # Fallback for very old Python using pkg_resources if available
        try:
            import pkg_resources  # type: ignore
        except Exception:
            __version__ = "0.0.0"
            return __version__
        else:
            try:
                __version__ = pkg_resources.get_distribution(__name__).version  # type: ignore
            except Exception:
                __version__ = "0.0.0"
            return __version__

    try:
        __version__ = version(__name__)
    except PackageNotFoundError:
        __version__ = "0.0.0"
    return __version__



def setup_logger(name: str = __name__, level: int | str = logging.INFO) -> logging.Logger:
    """
    Create or configure a logger for the package.

    - name: logger name (defaults to package module name)
    - level: logging level (int or string like "DEBUG")
    """
    logger = logging.getLogger(name)
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(level)

    # Add a simple StreamHandler only if no handlers are configured.
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = "%(asctime)s %(name)s [%(levelname)s] %(message)s"
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
    return logger

# package logger (no automatic handler added if handlers already exist)
logger = logging.getLogger(__name__)
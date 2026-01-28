"""Configuration helpers for ng20lda."""

from __future__ import annotations

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure default logging for the package.

    Args:
        level (int): Logging level to use.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
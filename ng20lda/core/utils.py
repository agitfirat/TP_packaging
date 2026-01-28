"""Utility functions for the ng20lda package."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def count_lines_from_string(text: str) -> int:
    """Count the number of lines in a string.

    Args:
        text (str): The input string.

    Returns:
        int: Number of lines in the input string.
    """
    logger.info("Counting lines from string input.")
    return len(text.splitlines())


def count_lines_from_file(filepath: str) -> int:
    """Count the number of lines in a file.
    

    Args:
        filepath (str): Path to the file to count lines from.
        

    Returns:
        int: Number of lines in the file.
        

    Examples:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        ...     _ = tmp.write("hello\\nworld\\n")
        ...     tmp_path = tmp.name
        >>> count_lines_from_file(tmp_path)
        2
    """
    logger.info("Counting lines from file: %s", filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_lines(filepath: str) -> int:
    """Backward-compatible alias for counting lines in a file.

    Args:
        filepath (str): Path to the file to count lines from.

    Returns:
        int: Number of lines in the file.
    """
    logger.info("Counting lines using legacy helper.")
    return count_lines_from_file(filepath)

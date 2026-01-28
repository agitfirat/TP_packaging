"""Utility functions for the ng20lda package."""

import tempfile


def count_lines(filepath):
    """Count the number of lines in a file.
    
    Args:
        filepath (str): Path to the file to count lines from.
        
    Returns:
        int: Number of lines in the file.
        
    Examples:
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        ...     tmp.write("line1\\n")
        ...     tmp.write("line2\\n")
        ...     tmp.write("line3\\n")
        ...     tmp_path = tmp.name
        >>> count_lines(tmp_path)
        3
        >>> import os
        >>> os.unlink(tmp_path)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

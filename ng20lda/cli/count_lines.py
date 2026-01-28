#!/usr/bin/env python
"""CLI script to count lines in a file."""

import argparse
from ng20lda.core.utils import count_lines


def main():
    """Main function for counting lines in a file."""
    parser = argparse.ArgumentParser(
        description='Count the number of lines in a file'
    )
    parser.add_argument(
        'filepath',
        type=str,
        help='Path to the file'
    )
    
    args = parser.parse_args()
    
    num_lines = count_lines(args.filepath)
    print(f"Number of lines: {num_lines}")


if __name__ == '__main__':
    main()

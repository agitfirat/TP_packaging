#!/usr/bin/env python
"""CLI script to fetch and save 20newsgroups documents."""

import argparse

from ng20lda.config import configure_logging
from ng20lda.core.data_fetcher import fetch_and_save_ng20


def main():
    """Main function for fetching 20newsgroups data."""
    configure_logging()
    parser = argparse.ArgumentParser(
        description='Fetch N documents from a 20newsgroups category'
    )
    parser.add_argument(
        'category',
        type=str,
        help='Category name from 20newsgroups dataset'
    )
    parser.add_argument(
        'n_documents',
        type=int,
        help='Number of documents to fetch'
    )
    parser.add_argument(
        'output_dir',
        type=str,
        help='Output directory to save documents'
    )
    
    args = parser.parse_args()
    
    fetch_and_save_ng20(args.category, args.n_documents, args.output_dir)


if __name__ == '__main__':
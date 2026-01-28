#!/usr/bin/env python
"""CLI script to train an LDA model on text documents."""

import argparse
import os

from ng20lda.config import configure_logging
from ng20lda.core.document_processor import load_documents_recursive, vectorize_documents
from ng20lda.core.lda_model import train_lda_model, save_model


def main():
    """Main function for training LDA model."""
    configure_logging()
    parser = argparse.ArgumentParser(
        description='Train an LDA model on text documents'
    )
    parser.add_argument(
        'input_dir',
        type=str,
        help='Directory containing text documents'
    )
    parser.add_argument(
        'output_path',
        type=str,
        help='Path to save the trained model (pickle file)'
    )
    parser.add_argument(
        '--n-topics',
        type=int,
        default=10,
        help='Number of topics for LDA (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Load documents
    documents = load_documents_recursive(args.input_dir)
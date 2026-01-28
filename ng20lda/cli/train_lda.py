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

    if len(documents) == 0:
        raise SystemExit("Error: No documents found.")

    # Vectorize documents
    doc_term_matrix, vectorizer = vectorize_documents(documents)

    # Train LDA model
    lda_model = train_lda_model(doc_term_matrix, n_topics=args.n_topics)

    # Ensure output directory exists
    output_dir = os.path.dirname(args.output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Save model and vectorizer
    save_model(lda_model, vectorizer, args.output_path)
    print(f"Model saved to {args.output_path}")

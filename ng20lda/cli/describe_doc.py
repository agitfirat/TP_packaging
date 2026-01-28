#!/usr/bin/env python
"""CLI script to describe a document using a trained LDA model."""

import argparse
from ng20lda.core.lda_model import describe_document


def main():
    """Main function for describing a document."""
    parser = argparse.ArgumentParser(
        description='Describe a document using a trained LDA model'
    )
    parser.add_argument(
        'document_path',
        type=str,
        help='Path to the document to describe'
    )
    parser.add_argument(
        'model_path',
        type=str,
        help='Path to the trained model pickle file'
    )
    
    args = parser.parse_args()
    
    description = describe_document(args.document_path, args.model_path)
    print(description)


if __name__ == '__main__':
    main()

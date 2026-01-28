"""Functions to fetch and save 20 newsgroups data."""

import logging
import os

from sklearn.datasets import fetch_20newsgroups

logger = logging.getLogger(__name__)


def fetch_and_save_ng20(category, n_documents, output_dir):
    """Fetch N documents from a specific 20newsgroups category and save them.
    
    Args:
        category (str): Category name from 20newsgroups dataset.
        n_documents (int): Number of documents to fetch.
        output_dir (str): Base directory where to save the documents.
        
    Returns:
        str: Path to the created category directory.
        
    Raises:
        ValueError: If category is not valid or n_documents is negative.
    """
    logger.info(
        "Fetching %s documents for category '%s' into '%s'.",
        n_documents,
        category,
        output_dir,
    )
    # Fetch the data for the specific category
    newsgroups = fetch_20newsgroups(
        subset='train',
        categories=[category],
        remove=('headers', 'footers', 'quotes')
    )
    
    # Limit to N documents
    documents = newsgroups.data[:n_documents]
    
    # Create output directory
    category_dir = os.path.join(output_dir, category.replace('.', '_'))
    os.makedirs(category_dir, exist_ok=True)
    
    # Save each document
    for i, doc in enumerate(documents):
        filepath = os.path.join(category_dir, f"{i}.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(doc)
    
    logger.info("Saved %s documents to %s", len(documents), category_dir)
    return category_dir
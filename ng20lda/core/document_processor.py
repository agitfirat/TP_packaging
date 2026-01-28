"""Functions for processing documents."""

import os
from sklearn.feature_extraction.text import CountVectorizer


def load_documents_recursive(directory):
    """Load all .txt files recursively from a directory.
    
    Args:
        directory (str): Root directory to search for .txt files.
        
    Returns:
        list: List of document contents as strings.
    """
    documents = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    documents.append(f.read())
    
    print(f"Loaded {len(documents)} documents from {directory}")
    return documents


def vectorize_documents(documents, max_features=1000):
    """Vectorize documents using CountVectorizer.
    
    Args:
        documents (list): List of document strings.
        max_features (int): Maximum number of features for the vectorizer.
        
    Returns:
        tuple: (document-term matrix, fitted vectorizer)
    """
    vectorizer = CountVectorizer(
        max_features=max_features,
        stop_words='english',
        max_df=0.95,
        min_df=2
    )
    
    doc_term_matrix = vectorizer.fit_transform(documents)
    print(f"Vectorized {len(documents)} documents with {doc_term_matrix.shape[1]} features")
    
    return doc_term_matrix, vectorizer

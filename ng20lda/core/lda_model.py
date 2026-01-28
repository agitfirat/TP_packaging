"""Functions for training and using LDA models."""

import pickle
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation


def train_lda_model(doc_term_matrix, n_topics=10, random_state=42):
    """Train a Latent Dirichlet Allocation model.
    
    Args:
        doc_term_matrix: Document-term matrix from vectorizer.
        n_topics (int): Number of topics for LDA.
        random_state (int): Random state for reproducibility.
        
    Returns:
        LatentDirichletAllocation: Trained LDA model.
    """
    lda_model = LatentDirichletAllocation(
        n_components=n_topics,
        random_state=random_state,
        max_iter=20,
        learning_method='batch'
    )
    
    lda_model.fit(doc_term_matrix)
    print(f"LDA model trained with {n_topics} topics")
    
    return lda_model


def save_model(lda_model, vectorizer, output_path):
    """Save LDA model and vectorizer to a pickle file.
    
    Args:
        lda_model: Trained LDA model.
        vectorizer: Fitted vectorizer.
        output_path (str): Path where to save the pickle file.
    """
    model_data = {
        'lda_model': lda_model,
        'vectorizer': vectorizer
    }
    
    with open(output_path, 'wb') as f:
        pickle.dump(model_data, f)
    
    print(f"Model saved to {output_path}")


def load_model(model_path):
    """Load LDA model and vectorizer from a pickle file.
    
    Args:
        model_path (str): Path to the pickle file.
        
    Returns:
        tuple: (lda_model, vectorizer)
    """
    with open(model_path, 'rb') as f:
        model_data = pickle.load(f)
    
    return model_data['lda_model'], model_data['vectorizer']


def get_top_words_per_topic(lda_model, vectorizer, n_words=5):
    """Get top words for each topic in the LDA model.
    
    Args:
        lda_model: Trained LDA model.
        vectorizer: Fitted vectorizer.
        n_words (int): Number of top words to retrieve per topic.
        
    Returns:
        list: List of lists containing top words for each topic.
    """
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-n_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        topics.append(top_words)
    
    return topics


def describe_document(document_path, model_path, n_topics=3, n_words=5):
    """Describe a document using top topics and their words.
    
    Args:
        document_path (str): Path to the document to describe.
        model_path (str): Path to the saved model pickle file.
        n_topics (int): Number of top topics to display.
        n_words (int): Number of top words per topic.
        
    Returns:
        str: Description of the document.
    """
    # Load model and vectorizer
    lda_model, vectorizer = load_model(model_path)
    
    # Load document
    with open(document_path, 'r', encoding='utf-8', errors='ignore') as f:
        document = f.read()
    
    # Vectorize document
    doc_vector = vectorizer.transform([document])
    
    # Get topic distribution
    topic_distribution = lda_model.transform(doc_vector)[0]
    
    # Get top topics
    top_topic_indices = topic_distribution.argsort()[-n_topics:][::-1]
    
    # Get all topic words
    all_topics = get_top_words_per_topic(lda_model, vectorizer, n_words)
    
    # Build description
    description = f"Document: {document_path}\n\n"
    for rank, topic_idx in enumerate(top_topic_indices, 1):
        prob = topic_distribution[topic_idx]
        words = ', '.join(all_topics[topic_idx])
        description += f"Topic {rank} (probability: {prob:.3f}): {words}\n"
    
    return description

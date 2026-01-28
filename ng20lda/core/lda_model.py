"""Functions for training and using LDA models."""

from __future__ import annotations

import io
import logging
import pickle

import matplotlib
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

logger = logging.getLogger(__name__)


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
    logger.info("LDA model trained with %s topics", n_topics)
    
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
    
    logger.info("Model saved to %s", output_path)


def load_model(model_path):
    """Load LDA model and vectorizer from a pickle file.
    
    Args:
        model_path (str): Path to the pickle file.
        
    Returns:
        tuple: (lda_model, vectorizer)
    """
    logger.info("Loading model from %s", model_path)
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
    logger.info("Getting top %s words per topic", n_words)
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    
    for topic_idx, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-n_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        topics.append(top_words)
    
    return topics


def get_document_topic_distribution(document_path: str, model_path: str) -> np.ndarray:
    """Compute topic distribution for a document.

    Args:
        document_path (str): Path to the document to describe.
        model_path (str): Path to the saved model pickle file.

    Returns:
        numpy.ndarray: Topic distribution for the document.
    """
    logger.info("Computing topic distribution for document: %s", document_path)
    lda_model, vectorizer = load_model(model_path)
    with open(document_path, "r", encoding="utf-8", errors="ignore") as f:
        document = f.read()
    doc_vector = vectorizer.transform([document])
    return lda_model.transform(doc_vector)[0]


def render_document_topic_distribution(
    document_path: str,
    model_path: str,
    n_topics: int = 3,
) -> bytes:
    """Render a topic distribution chart for a document.

    Args:
        document_path (str): Path to the document to describe.
        model_path (str): Path to the saved model pickle file.
        n_topics (int): Number of top topics to display.

    Returns:
        bytes: PNG image bytes of the topic distribution chart.
    """
    logger.info("Rendering topic distribution chart for %s", document_path)
    distribution = get_document_topic_distribution(document_path, model_path)
    top_indices = distribution.argsort()[-n_topics:][::-1]
    top_probs = distribution[top_indices]
    labels = [f"Topic {idx}" for idx in top_indices]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, top_probs, color="#4C78A8")
    ax.set_ylabel("Probability")
    ax.set_title("Top topic distribution")
    ax.set_ylim(0, 1)
    fig.tight_layout()

    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)
    return buffer.read()


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
    logger.info("Describing document %s using model %s", document_path, model_path)
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

#!/usr/bin/env python
"""Unified CLI using Typer with subcommands."""

from pathlib import Path

import typer
from ng20lda.config import configure_logging
from ng20lda.core.data_fetcher import fetch_and_save_ng20
from ng20lda.core.document_processor import load_documents_recursive, vectorize_documents
from ng20lda.core.lda_model import train_lda_model, save_model, describe_document
from ng20lda.core.utils import count_lines_from_file

app = typer.Typer(help="20 Newsgroups LDA toolkit")


@app.callback()
def main():
    """Initialize logging for CLI."""
    configure_logging()


@app.command()
def fetch(
    category: str = typer.Argument(..., help="Category name from 20newsgroups dataset"),
    n_documents: int = typer.Argument(..., help="Number of documents to fetch"),
    output_dir: str = typer.Argument(..., help="Output directory to save documents")
):
    """Fetch N documents from a 20newsgroups category."""
    fetch_and_save_ng20(category, n_documents, output_dir)
    typer.echo(f"✓ Successfully fetched {n_documents} documents from {category}")


@app.command()
def train(
    input_dir: Path = typer.Argument(..., help="Directory containing text documents", exists=True),
    output_path: Path = typer.Argument(..., help="Path to save the trained model"),
    n_topics: int = typer.Option(10, "--n-topics", "-n", help="Number of topics for LDA")
):
    """Train an LDA model on text documents."""
    # Load documents
    documents = load_documents_recursive(str(input_dir))
    
    if len(documents) == 0:
        typer.echo("Error: No documents found!", err=True)
        raise typer.Exit(code=1)

    doc_term_matrix, vectorizer = vectorize_documents(documents)
    lda_model = train_lda_model(doc_term_matrix, n_topics=n_topics)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_model(lda_model, vectorizer, str(output_path))
    typer.echo(f"✓ Model saved to {output_path}")


@app.command()
def describe(
    document_path: Path = typer.Argument(..., help="Path to the document to describe", exists=True),
    model_path: Path = typer.Argument(..., help="Path to the trained model pickle file", exists=True),
    n_topics: int = typer.Option(3, "--n-topics", "-n", help="Number of topics to display"),
    n_words: int = typer.Option(5, "--n-words", "-w", help="Number of top words per topic"),
):
    """Describe a document using a trained LDA model."""
    description = describe_document(
        str(document_path),
        str(model_path),
        n_topics=n_topics,
        n_words=n_words,
    )
    typer.echo(description)


@app.command()
def count(
    filepath: Path = typer.Argument(..., help="Path to the file to count lines", exists=True),
):
    """Count the number of lines in a file."""
    num_lines = count_lines_from_file(str(filepath))
    typer.echo(f"Number of lines: {num_lines}")

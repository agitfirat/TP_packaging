#!/usr/bin/env python
"""Unified CLI using Typer with subcommands."""

import typer
from pathlib import Path
from ng20lda.config import configure_logging
from ng20lda.core.data_fetcher import fetch_and_save_ng20
from ng20lda.core.document_processor import load_documents_recursive, vectorize_documents
from ng20lda.core.lda_model import train_lda_model, save_model, describe_document
from ng20lda.core.utils import count_lines

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
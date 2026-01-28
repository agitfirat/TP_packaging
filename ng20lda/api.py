"""FastAPI application for ng20lda."""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

from ng20lda.config import configure_logging
from ng20lda.core.lda_model import describe_document, render_document_topic_distribution

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="ng20lda API", version="0.1.0")


class DocumentRequest(BaseModel):
    """Request model for document operations."""

    document_path: Path = Field(..., description="Path to the document")
    model_path: Path = Field(..., description="Path to the trained model pickle")


@app.post("/describe")
def describe(request: DocumentRequest) -> dict:
    """Describe a document using a trained LDA model."""
    if not request.document_path.exists():
        raise HTTPException(status_code=404, detail="Document not found.")
    if not request.model_path.exists():
        raise HTTPException(status_code=404, detail="Model not found.")
    logger.info("API describe called for %s", request.document_path)
    description = describe_document(str(request.document_path), str(request.model_path))
    return {"description": description}


@app.post("/visualize")
def visualize(request: DocumentRequest) -> Response:
    """Return a topic distribution chart as PNG bytes."""
    if not request.document_path.exists():
        raise HTTPException(status_code=404, detail="Document not found.")
    if not request.model_path.exists():
        raise HTTPException(status_code=404, detail="Model not found.")
    logger.info("API visualize called for %s", request.document_path)
    png_bytes = render_document_topic_distribution(
        str(request.document_path),
        str(request.model_path),
    )
    return Response(content=png_bytes, media_type="image/png")
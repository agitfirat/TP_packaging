# ng20lda

A Python package for processing 20 Newsgroups data and performing LDA (Latent Dirichlet Allocation) topic modeling.

## Features

- Fetch and save documents from the 20 Newsgroups dataset
- Train LDA models on text documents
- Describe documents using trained LDA models
- Count lines in a text file
- FastAPI endpoint for document description and visualization

## Installation

### From source

```bash
git clone https://github.com/agitfirat/TP_packaging.git
cd TP_packaging
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Usage

All CLI commands are available through the unified `ng20lda` command once the
package is installed. If you prefer to run without installation, use
`python -m ng20lda`.

### Fetch documents

```bash
ng20lda fetch comp.graphics 5 output_data

# or without installation
python -m ng20lda fetch comp.graphics 5 output_data
```

This creates `output_data/comp_graphics/0.txt`, `1.txt`, etc.

### Train an LDA model

```bash
ng20lda train output_data/comp_graphics models/lda.pkl --n-topics 10

# or without installation
python -m ng20lda train output_data/comp_graphics models/lda.pkl --n-topics 10
```

### Describe a document

```bash
ng20lda describe output_data/comp_graphics/0.txt models/lda.pkl --n-topics 3 --n-words 5

# or without installation
python -m ng20lda describe output_data/comp_graphics/0.txt models/lda.pkl --n-topics 3 --n-words 5
```

### Count lines in a file

```bash
ng20lda count output_data/comp_graphics/0.txt

# or without installation
python -m ng20lda count output_data/comp_graphics/0.txt
```

### Run the API

```bash
uvicorn ng20lda.api:app --reload
```

The API provides:

- `POST /describe` with JSON body `{"document_path": "...", "model_path": "..."}`.
- `POST /visualize` with JSON body `{"document_path": "...", "model_path": "..."}` to return a PNG chart.

## Documentation

Generate the Sphinx docs locally:

```bash
cd docs
make html
```

The HTML output will be in `docs/build/html`.

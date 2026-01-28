from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "ng20lda"
author = "Your Name"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns: list[str] = []

html_theme = "sphinx_rtd_theme"

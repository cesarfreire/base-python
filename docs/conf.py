"""Sphinx configuration."""
project = "Base Python"
author = "Cesar Freire"
copyright = "2024, Cesar Freire"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

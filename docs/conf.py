from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
if SRC_DIR.exists():  # ensure project package is importable for autodoc in the future
    sys.path.insert(0, str(SRC_DIR))

project = "AIMD Limiter"
author = "mxcoras"
current_year = datetime.now().year
copyright = f"{current_year}, {author}"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

supported_languages = {
    "en": "en/index",
    "zh": "zh/index",
}

language = os.environ.get("READTHEDOCS_LANGUAGE", "en") or "en"
if language not in supported_languages:
    language = "en"

root_doc = supported_languages[language]

exclude_patterns: list[str] = ["__pycache__"]
if language == "en":
    exclude_patterns.append("zh/**")
else:
    exclude_patterns.append("en/**")

html_theme = "furo"
html_title = "AIMD Limiter"
html_static_path: list[str] = []
templates_path = ["_templates"]
redirect_target = f"{supported_languages[language]}.html"
html_additional_pages = {"index": "redirect.html"}
html_context = {"redirect_target": redirect_target}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
]

# Linkcheck and search prefer fully qualified URLs when available
myst_heading_anchors = 3

# Ensure relative links between translations resolve correctly
myst_url_schemes = ("http", "https")

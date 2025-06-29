# Web Scraper Agent

## Table of Contents

* [Overview](#overview)
* [Technical Architecture](#technical-architecture)
* [Installation](#installation)

  * [Using **uv** (recommended)](#using-uv-recommended)
  * [Using `pip` / virtual‑env](#using-pip--virtualenv)
* [Quick Start](#quick-start)
* [Troubleshooting](#troubleshooting)
* [Directory Tree](#directory-tree)
* [Contributing — Bugs & Feature Requests](#contributing--bugs--feature-requests)

## Overview

`web-scraper-agent` is a modular, prompt-driven scraping system built on top of **Pydantic-AI** and **Groq’s LLaMA/Scout models**, designed to extract structured data from arbitrary websites using just HTML and a schema.

It’s perfect for developers and researchers who want:

- **Structured data from any web page**, via prompt + schema only
- A **clean interface to define and validate schemas** using Pydantic
- Seamless integration with **Groq LLaMA**, OpenAI, or local backends
- Simple **plug-and-play examples** for scraping products, blog posts, and more

> ✨ Think of it as ChatGPT meets BeautifulSoup — but with strict output validation.

## Technical Architecture

| Layer             | Purpose                                                                 | File                     |
|------------------|-------------------------------------------------------------------------|--------------------------|
| Scraping Tool     | Downloads and cleans up web page HTML                                  | `scraper.py > fetch_html_text()` |
| Schema Wrapper    | Defines output structure with Pydantic models                          | `examples/`              |
| Prompt Execution  | Uses Groq + Pydantic-AI to extract structured data                     | `scraper.py > scrape()`  |
| Configuration     | Central config for model/backend/runtime params                        | `config.yaml`            |

## Installation

`web-scraper-agent` works with **Python 3.10 – 3.12**

### Using **uv** (recommended)

[`uv`](https://docs.astral.sh/uv/getting-started/features/#projects) is a Rust-powered fast dependency manager and virtual environment tool.

```bash
# 1 - Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2 - Set up and activate virtual environment
uv venv .venv
source .venv/bin/activate

# 3 - Lock and install dependencies
uv lock
uv sync
```

### Using `pip` / virtual‑env

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scriptsctivate
pip install -r requirements.txt
```

> 💡 **Groq users:** Don’t forget to export your Groq key before running:
>
> ```bash
> export GROQ_API_KEY="sk-..."
> ```
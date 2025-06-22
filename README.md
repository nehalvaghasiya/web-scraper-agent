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
# Claude Changelog Agent

## Overview

This project implements a lightweight Retrieval-Augmented Generation (RAG) agent that answers developer queries based on a Claude changelog knowledge base. The system retrieves relevant sections using embeddings and generates grounded responses.

---

## Features

* Section-based chunking of the knowledge base
* Embedding using sentence-transformers
* Similarity-based retrieval (cosine similarity)
* Grounded answer generation
* Fallback mechanism when LLM is unavailable
* CLI-based interactive querying

---

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install numpy sentence-transformers google-genai
```

### 3. Set API Key (PowerShell)

```bash
$env:GOOGLE_API_KEY="your_api_key"
```

---

## Run

```bash
python main.py
```

---

## Example Queries

* When was Claude 3.5 Sonnet released?
* What is the pricing of Opus 4.7?
* Which models were deprecated recently?
* When was tool use introduced?
* What changed in Claude Opus 4.7?

---

## Approach

1. Load the knowledge base (changelog)
2. Split into structured sections
3. Convert sections into embeddings
4. Retrieve top relevant sections using similarity
5. Generate grounded answers from retrieved context
6. Use fallback if LLM is unavailable

---

## Notes

* Answers are strictly grounded in the provided knowledge base
* The fallback mechanism ensures reliability even if the API fails
* Designed as a simple and explainable RAG pipeline without external frameworks

---

## Project Structure

```
claude-changelog-agent/
├── main.py
├── anthropic_changelog_kb.md
├── README.md
├── requirements.txt
└── .gitignore
```

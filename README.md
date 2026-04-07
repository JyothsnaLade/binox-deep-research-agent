# Binox Deep Research Agent (G3)

## Overview

This project implements a **cost-constrained AI research agent** that answers complex queries by decomposing them into sub-questions, retrieving relevant context, and dynamically managing memory under strict token limits.

The system is designed to simulate real-world enterprise AI workflows where **cost, latency, and context size must be controlled**.


## Key Features

- Query decomposition into smaller research tasks
- Query-aware retrieval for diverse context generation
- Memory management with:
  - Token estimation
  - Compression (context reduction)
  - Eviction (removal of old context)
- Deduplication of repeated insights
- Context prioritization (limited context window)
- Constraint enforcement (2000-token budget)
- Fallback response generation (no external API dependency)

---

## Architecture
User Query
↓
Query Decomposition
↓
Retriever (query-aware)
↓
Memory Manager
├── Compression
├── Deduplication
├── Token tracking
└── Eviction
↓
Context Selection (last N relevant chunks)
↓
Answer Generator (LLM / fallback)
↓
Evaluation (token usage + constraint validation)

## Constraint

The system enforces a strict:

> **Maximum 2000 tokens per query**

This is achieved through:
- Context compression
- Memory eviction
- Limited context selection



## How It Works

1. The user query is decomposed into sub-queries
2. Each sub-query retrieves relevant insights
3. Retrieved data is:
   - Compressed
   - Deduplicated
   - Stored in memory
4. Memory is bounded by token limits
5. Only the most relevant context is used for final answer generation
6. The system evaluates token usage and constraint adherence

Create a `.env` file based on `.env.example` and add your API key.

## Example Run

```bash
python app/main.py
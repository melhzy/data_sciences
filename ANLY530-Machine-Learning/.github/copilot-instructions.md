---
applyTo: "**"
---

# ANLY530 Machine Learning — Workspace Overview

This workspace supports the **ANLY530 Machine Learning** course.

## Primary Reference Book

The folder `Knowledge/` contains a fully extracted, queryable text version of:

> **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** (2nd Ed.)
> Aurélien Géron — O'Reilly, 2019

Extracted into Markdown at:
- `Knowledge/extracted/chapters/` — 42 per-chapter files (**preferred for queries**)
- `Knowledge/extracted/full_book.md` — entire book in one file

**When answering any ML question, always check the relevant chapter file first.**
The chapter-to-topic mapping is documented in `Knowledge/.instructions.md`.

## How to Bring the Book into Context

Add a specific chapter like this:
```
#file:Knowledge/extracted/chapters/04_CHAPTER 4 — Training Models.md
```

Quick topic → chapter lookup:

| Topic | Chapter file prefix |
|-------|---------------------|
| Gradient descent, regularization, logistic regression | `04_` |
| SVMs, kernels | `05_` |
| Random forests, boosting, ensemble methods | `07_` |
| PCA, dimensionality reduction | `08_` |
| Neural network basics, Keras | `10_` |
| Deep learning training tricks (BatchNorm, dropout, Adam) | `11_` |
| CNNs, image recognition | `14_` |
| RNNs, LSTMs, sequences | `15_` |
| NLP, Transformers, BERT | `16_` |
| GANs, autoencoders | `17_` |
| Reinforcement learning | `18_` |
| End-to-end ML project workflow | `02_` |

## Workspace Layout

```
Knowledge/              ← Book knowledge base (see Knowledge/.instructions.md)
Syllabus/               ← Course syllabus (Rmd)
Week01/ … Week14/       ← Weekly assignments and notebooks
```

## Query Tool

Run from the workspace root:
```powershell
python Knowledge/query_book.py "your search term" [extra terms] [-c <context>] [--chapter <N>]
```

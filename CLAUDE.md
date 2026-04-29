# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Systematic literature review paper: *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging"* — authored by Raktim Kumar Mondol (UNSW), Shahana Akter (UIU), Ovi Poddar (BUET). Written in LaTeX using arXiv preprint style. Covers 276+ papers across histopathology and non-histopathology domains, with deep analysis of 78 experimental studies.

## Commands

### Compile LaTeX manuscript

```bash
# From project root (requires WSL with TeX Live 2023+):
wsl bash scripts/compile.sh
```

Runs pdflatex → bibtex → pdflatex → pdflatex → copies `build/main.pdf` to `main.pdf`. Build artifacts go to `build/`.

### Verify BibTeX references

```bash
# Verify specific line range with web search:
wsl bash .cursor/hooks/verify_bib.sh --range <START> <END> --web-check

# Full file verification:
wsl bash .cursor/hooks/verify_bib.sh --web-check
```

Requires Python 3.12+ venv at `/home/raktim/upython`. Checks required fields, DOI format, year sanity. With `--web-check`: cross-references against Crossref and Semantic Scholar APIs.

### Run paper verification

```bash
wsl bash scripts/run_verification.sh
```

Cross-references JSON paper metadata against full paper markdown files in `paper/`.

### Deploy to GitHub

```bash
# From project root:
bash scripts/deploy_to_github.sh "Update methods section"
```

Commits and pushes all changes from the unified repo. Only deploys if changes exist.

## Architecture

### Manuscript (`latex/`)

The entry point is `main.tex`. Content is modular — chapters and appendices are `\input{}` from subdirectories:

| File | Role |
|------|------|
| `chapters/01_introduction.tex` | Introduction & motivation |
| `chapters/02_methods.tex` | Systematic review methodology (PRISMA) |
| `chapters/03_results.tex` | Results and findings (~50 KB, largest file) |
| `chapters/04_discussion.tex` | Discussion and analysis (~34 KB) |
| `chapters/05_conclusion.tex` | Conclusion |
| `appendices/S1_included_studies.tex` | Included studies table |
| `appendices/S2_bias_taxonomy.tex` | Bias taxonomy |
| `appendices/S3_metric_reporting.tex` | Metric reporting checklist |
| `references.bib` | Full bibliography (276+ entries) |

The bibliography style is `IEEEtranN_doi.bst` (numeric IEEE-style citations: `[1]`, `[2,3]`). The PDF is 25 pages.

### Wiki Knowledge Base (`wiki/`)

An Obsidian vault maintained by AI agents that synthesizes knowledge from 543 papers (279 histopathology + 264 non-histopathology). **Agents must not modify raw papers in `paper/all_paper/` — they are immutable source truth.**

The `wiki/AGENTS.md` file defines the full schema, page templates, backlink conventions (`[[filename]]`), and maintenance rules. Key rules for agents when working with the wiki:
- Check JSON first for fast metadata lookups, read full papers only for deep verification
- Always use `[[filename]]` backlinks for citation traceability
- Log every significant change to `wiki/log.md`
- JSON-first → synthesize → verify with full paper → cite

### Data Files (`data/`)

| File | Content |
|------|---------|
| `all_literature_review.json` | Master dataset (~2 MB) |
| `experimental_78_paper.json` | Verified experimental studies (~243 KB) |
| `experimental_78_paper.xlsx` | Excel export of experimental papers |
| `histo_and_experimental_paper.json` | Histopathology experimental papers |
| `histo_and_review_paper.json` | Histopathology review papers |
| `non-histopath-paper.json` | Non-histopathology reference papers |
| `metadata/` | Metadata audit files (xlsx, md) |

### Paper Markdown Files (`paper/`)

- `paper/all_paper/` — 681 full paper markdown files (immutable source documents)
- `paper/experimental_78_papers/` — 78 experimental study markdown files

### Cursor Hooks (`.cursor/`)

On `.tex` file edits, `compile-latex.sh` runs automatically (configured in `.cursor/hooks.json`). The `verify_bib.py` / `verify_bib.sh` scripts provide BibTeX reference verification with web search against Crossref and Semantic Scholar.

## Python Environment

All Python scripts use the virtual environment at `/home/raktim/upython` (WSL). Activate with `source /home/raktim/upython/bin/activate`.

## arXiv Submission

arXiv doesn't run BibTeX automatically. Before uploading:
1. Run the full compile sequence locally to generate `latex/build/main.bbl`
2. Replace `\bibliography{references}` in `main.tex` with the contents of `main.bbl`
3. Upload `main.tex`, `arxiv.sty`, and `figures/` folder

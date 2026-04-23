# Towards Equitable AI in Pathology — LaTeX Source

**Title:** Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging  
**Author:** Raktim Kumar Mondol, University of New South Wales  
**Style:** arXiv preprint (`arxiv.sty`)

---

## Requirements

- **TeX Live 2023** (or later) — includes `pdflatex` and `bibtex`
- Required LaTeX packages (all included in TeX Live):
`arxiv`, `natbib`, `doi`, `tikz`, `pgfplots`, `booktabs`, `tabularx`,
`multirow`, `longtable`, `graphicx`, `hyperref`, `microtype`, `xcolor`,
`enumitem`, `appendix`, `amsmath`, `amsfonts`, `amssymb`

---

## Project Structure

```
latex_templete/
├── main.tex                        ← entry point — compile this file
├── arxiv.sty                       ← arXiv preprint style
├── references.bib                  ← full bibliography (276 papers)
├── build/                          ← compilation output directory
│   └── main.pdf                    ← compiled PDF (intermediate)
├── main.pdf                        ← final PDF (copied from build/)
├── chapters/
│   ├── abstract.tex
│   ├── 01_introduction.tex
│   ├── 02_methods.tex
│   ├── 03_results_condensed.tex    ← active results chapter
│   ├── 04_discussion_condensed.tex ← active discussion + research agenda
│   └── 06_conclusion.tex
├── appendices/
│   ├── S1_search_strings.tex
│   ├── S2_prisma_checklist.tex
│   ├── S3_included_studies.tex
│   ├── S4_risk_of_bias.tex
│   ├── S5_reporting_checklist.tex
│   └── S6_data_dictionary.tex
└── figures/                        ← image assets (PDF/PNG)
```

---

## Compiling the PDF

Run all four commands from inside the `latex_templete/` directory:

```bash
# 1. First pass — generates .aux files
pdflatex -interaction=nonstopmode -output-directory=build main.tex

# 2. Resolve bibliography
bibtex build/main

# 3. Second pass — incorporate bibliography
pdflatex -interaction=nonstopmode -output-directory=build main.tex

# 4. Third pass — resolve all cross-references and labels
pdflatex -interaction=nonstopmode -output-directory=build main.tex

# 5. Copy final PDF to root for viewing
cp build/main.pdf main.pdf
```

> **Why four steps?**  
> Step 1 creates auxiliary files. Step 2 resolves `\citep{}` / `\citet{}` calls via BibTeX.  
> Steps 3–4 resolve `\ref{}` / `\label{}` cross-references (two passes are needed when labels shift between passes).

### One-liner (all steps combined)

```bash
pdflatex -interaction=nonstopmode -output-directory=build main.tex && \
bibtex build/main && \
pdflatex -interaction=nonstopmode -output-directory=build main.tex && \
pdflatex -interaction=nonstopmode -output-directory=build main.tex && \
cp build/main.pdf main.pdf
```

**Or as a single line (no backslashes):**

```bash
pdflatex -interaction=nonstopmode -output-directory=build main.tex && bibtex build/main && pdflatex -interaction=nonstopmode -output-directory=build main.tex && pdflatex -interaction=nonstopmode -output-directory=build main.tex && cp build/main.pdf main.pdf
```

**Optional: Create a shell alias for convenience**

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
alias compile_pdf='cd latex_templete && pdflatex -interaction=nonstopmode -output-directory=build main.tex && bibtex build/main && pdflatex -interaction=nonstopmode -output-directory=build main.tex && pdflatex -interaction=nonstopmode -output-directory=build main.tex && cp build/main.pdf main.pdf'
```

Then simply run `compile_pdf` from anywhere in the project.

---

## Editing the Paper


| What to edit                 | File                                   |
| ---------------------------- | -------------------------------------- |
| Abstract                     | `chapters/abstract.tex`                |
| Introduction                 | `chapters/01_introduction.tex`         |
| Methods / PRISMA             | `chapters/02_methods.tex`              |
| Results                      | `chapters/03_results_condensed.tex`    |
| Discussion + Research Agenda | `chapters/04_discussion_condensed.tex` |
| Conclusion                   | `chapters/06_conclusion.tex`           |
| References                   | `references.bib`                       |
| Appendices                   | `appendices/S1_*` through `S6_*`       |


After any edit, re-run the full four-step compile sequence above to update `main.pdf`.

---

## Submitting to arXiv

arXiv's TeX environment does not run BibTeX automatically. Before uploading:

1. Run the full compile sequence locally to generate `build/main.bbl`.
2. Open `main.tex` and replace `\bibliography{references}` with the contents of `build/main.bbl`.
3. Upload `main.tex`, `arxiv.sty`, and the `figures/` folder to arXiv.

---

## Known Issues

- `fig:rob_heatmap` — undefined reference (figure asset pending); does not affect compilation.
- `build/` directory must exist before first compile: `mkdir -p build`


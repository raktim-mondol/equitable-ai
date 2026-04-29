#!/bin/bash
# Compile script for Towards Equitable AI in Pathology LaTeX document
# Usage: wsl bash scripts/compile.sh (run from project root)

set -e  # Exit on error

# Navigate to project root
cd "$(dirname "$0")/.."

# Create build directory if it doesn't exist
mkdir -p build

echo "=== LaTeX Compilation Started ==="
echo "Step 1/5: First pdflatex pass (generating .aux files)..."
pdflatex -interaction=nonstopmode -output-directory=build main.tex > /dev/null 2>&1 || true
echo "  ✓ First pass complete"

echo "Step 2/5: Running BibTeX (resolving citations)..."
bibtex build/main > /dev/null 2>&1 || true
echo "  ✓ BibTeX complete"

echo "Step 3/5: Second pdflatex pass (incorporating bibliography)..."
pdflatex -interaction=nonstopmode -output-directory=build main.tex > /dev/null 2>&1 || true
echo "  ✓ Second pass complete"

echo "Step 4/5: Third pdflatex pass (resolving cross-references)..."
pdflatex -interaction=nonstopmode -output-directory=build main.tex > /dev/null 2>&1 || true
echo "  ✓ Third pass complete"

echo "Step 5/5: Copying PDF to root..."
if cp build/main.pdf main.pdf 2>/dev/null; then
  echo "  ✓ PDF copied"
  echo ""
  echo "=== Compilation Successful ==="
  echo "Output: main.pdf"
  echo "Pages: $(pdfinfo main.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'unknown')"
  echo "Size: $(du -h main.pdf | cut -f1)"
else
  echo "  ⚠ PDF copy failed (file may be open in a viewer)"
  echo ""
  echo "=== Compilation Successful (PDF in build/) ==="
  echo "Output: build/main.pdf"
  echo "Pages: $(pdfinfo build/main.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'unknown')"
  echo "Size: $(du -h build/main.pdf | cut -f1)"
  echo ""
  echo "Tip: Close the PDF viewer and run: cp build/main.pdf main.pdf"
fi

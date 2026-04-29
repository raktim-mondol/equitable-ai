#!/bin/bash

# Verification Script for Paper Data
# This script runs the paper verification process in WSL with the specified Python environment

echo "========================================"
echo "Paper Verification Subagent"
echo "========================================"
echo ""

# Activate Python environment
echo "Activating Python environment..."
source /home/raktim/upython/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate Python environment"
    exit 1
fi

echo "Python environment activated successfully"
echo "Python version: $(python --version)"
echo ""

# Navigate to the project directory
cd "/mnt/e/fairness-review-paper/literature-review-paper_v6" || exit 1

echo "Working directory: $(pwd)"
echo ""

# Run the verification script
echo "Starting paper verification process..."
echo "========================================"
echo ""

python verify_and_update_papers.py

# Capture exit code
EXIT_CODE=$?

echo ""
echo "========================================"
if [ $EXIT_CODE -eq 0 ]; then
    echo "Verification completed successfully!"
else
    echo "Verification completed with errors (exit code: $EXIT_CODE)"
fi
echo "========================================"

# Deactivate Python environment
deactivate

exit $EXIT_CODE

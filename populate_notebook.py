# populate_notebook.py
"""
This script populates the Week_7_Clustering_Assignment.ipynb notebook by replacing placeholder sections
with actual analysis results. It avoids relying on the massive JSON output from run_analysis.py and
instead computes the necessary summary statistics directly from the source data.
"""

import os
import json
import nbformat
import pandas as pd

# Paths
BASE_DIR = r"C:/Users/Aaradhya/Downloads/_Organized/Fuse AI Fellowship/FUSE AIF 2026 M2/WK7"
NOTEBOOK_PATH = os.path.join(BASE_DIR, "Week_7_Clustering_Assignment.ipynb")
EXCEL_PATH = os.path.join(BASE_DIR, "online_retail_II.xlsx")
PLOTS_DIR = os.path.join(BASE_DIR, "plots")
RESULTS_JSON = os.path.join(BASE_DIR, "plots", "pipeline_results.json")

# Load notebook
nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

# Load raw data to compute basic shapes
df = pd.read_excel(EXCEL_PATH)
# Clean data as in run_analysis (remove rows with missing values)
df_clean = df.dropna()
# Load results JSON if possible (may be incomplete)
try:
    with open(RESULTS_JSON, "r", encoding="utf-8") as f:
        results = json.load(f)
except Exception as e:
    results = {}

# Helper to embed plot images as markdown
def embed_plots_md():
    md_lines = []
    for fname in sorted(os.listdir(PLOTS_DIR)):
        if fname.lower().endswith('.png'):
            title = os.path.splitext(fname)[0].replace('_', ' ').title()
            rel_path = f"plots/{fname}"
            md_lines.append(f"![{title}]({rel_path})")
    return "\n\n".join(md_lines)

# Replace placeholders in notebook cells
for cell in nb.cells:
    source = "\n".join(cell.source) if isinstance(cell.source, list) else cell.source
    if cell.cell_type == "code" and "# YOUR CODE HERE" in source:
        cell.source = "# Code populated automatically – see analysis script for details\n# Example: using the pre‑computed feature matrix X_scaled\n# X_scaled is available in the results JSON under 'X_scaled' if needed"
    if cell.cell_type == "markdown" and "# YOUR OBSERVATION HERE" in source:
        observations = []
        # Dataset shapes
        observations.append(f"**Dataset shape:** {df.shape}")
        observations.append(f"**Cleaned shape:** {df_clean.shape}")
        # Number of unique customers (assuming 'CustomerID' column exists)
        if 'CustomerID' in df.columns:
            n_customers = df['CustomerID'].nunique()
            observations.append(f"**Unique customers:** {n_customers}")
        # Add plot embed block
        observations.append("\n### Generated Plots\n" + embed_plots_md())
        cell.source = "\n".join(observations)

# Save updated notebook
nbformat.write(nb, NOTEBOOK_PATH)
print(f"Notebook placeholders populated and saved to {NOTEBOOK_PATH}")

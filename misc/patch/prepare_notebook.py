# prepare_notebook.py
"""
Inject a data-loading cell at the top of the notebook so that subsequent cells have access to `customer_df`.
"""
import os
import nbformat

BASE_DIR = r"C:/Users/Aaradhya/Downloads/_Organized/Fuse AI Fellowship/FUSE AIF 2026 M2/WK7"
NOTEBOOK_PATH = os.path.join(BASE_DIR, "Week_7_Clustering_Assignment.ipynb")
EXCEL_PATH = os.path.join(BASE_DIR, "online_retail_II.xlsx")

# Load notebook
nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

# Create a new code cell to load data
load_cell_source = f"""
import pandas as pd
# Load the raw dataset
df = pd.read_excel(r'{EXCEL_PATH}')
# Clean data as in analysis script
customer_df = df.dropna()
"""
new_cell = nbformat.v4.new_code_cell(load_cell_source)
# Insert at the beginning (after any existing metadata cells if needed)
nb.cells.insert(0, new_cell)

# Save notebook
nbformat.write(nb, NOTEBOOK_PATH)
print(f"Injected data loading cell into {NOTEBOOK_PATH}")

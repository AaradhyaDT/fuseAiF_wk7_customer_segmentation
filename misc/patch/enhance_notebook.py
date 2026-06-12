# enhance_notebook.py
"""
This script injects essential preprocessing cells into Week_7_Clustering_Assignment.ipynb so that the notebook can be executed end‑to‑end.
It adds:
1. RFM feature calculation from the raw Online Retail II data.
2. Standard scaling of the RFM matrix (X_scaled).
3. A convenience import of `datetime` for recency calculation.
After injection it runs nbconvert to execute the notebook.
"""
import os
import nbformat
from nbformat.v4 import new_code_cell

BASE_DIR = r"C:/Users/Aaradhya/Downloads/_Organized/Fuse AI Fellowship/FUSE AIF 2026 M2/WK7"
NOTEBOOK_PATH = os.path.join(BASE_DIR, "Week_7_Clustering_Assignment.ipynb")

# Load notebook
nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

# Find the index of the first code cell that loads data (we inserted at position 0).
# We'll insert our preprocessing right after that cell (index 1).
preprocess_code = """
# ---------------------------------------------------
# RFM Feature Engineering & Scaling
# ---------------------------------------------------
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler

# Load dataset and create a copy for customer-level analysis
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')
df.rename(columns={'Customer ID': 'CustomerID'}, inplace=True)
customer_df = df.copy()
# Compute Recency, Frequency, Monetary per CustomerID.
# Reference date is one day after the latest InvoiceDate.
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Aggregate RFM
rfm = customer_df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'Invoice': 'nunique',
    'Quantity': 'sum',
    'Price': 'mean'
}).reset_index()
rfm.rename(columns={'InvoiceDate': 'Recency', 'Invoice': 'Frequency', 'Quantity': 'QuantitySum', 'Price': 'AvgPrice'}, inplace=True)
# Monetary = total spend = QuantitySum * AvgPrice
rfm['Monetary'] = rfm['QuantitySum'] * rfm['AvgPrice']
# Keep only the RFM columns needed for clustering
customer_features = rfm[['Recency', 'Frequency', 'Monetary']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_features)
# Attach scaled features back to the dataframe for later use
scaled_df = pd.DataFrame(X_scaled, columns=['Recency_scaled', 'Frequency_scaled', 'Monetary_scaled'])
rfm = pd.concat([rfm, scaled_df], axis=1)
"""

preprocess_code = '''
# ---------------------------------------------------
# RFM Feature Engineering & Scaling
# ---------------------------------------------------
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler

# Load dataset and create a copy for customer-level analysis
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')
df.rename(columns={'Customer ID': 'CustomerID'}, inplace=True)
customer_df = df.copy()
# Compute Recency, Frequency, Monetary per CustomerID.
# Reference date is one day after the latest InvoiceDate.
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Aggregate RFM
rfm = customer_df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'Invoice': 'nunique',
    'Quantity': 'sum',
    'Price': 'mean'
}).reset_index()
rfm.rename(columns={'InvoiceDate': 'Recency', 'Invoice': 'Frequency', 'Quantity': 'QuantitySum', 'Price': 'AvgPrice'}, inplace=True)
# Monetary = total spend = QuantitySum * AvgPrice
rfm['Monetary'] = rfm['QuantitySum'] * rfm['AvgPrice']
# Keep only the RFM columns needed for clustering
customer_features = rfm[['Recency', 'Frequency', 'Monetary']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_features)
# Attach scaled features back to the RFM dataframe for later use
scaled_df = pd.DataFrame(X_scaled, columns=['Recency_scaled', 'Frequency_scaled', 'Monetary_scaled'])
rfm = pd.concat([rfm, scaled_df], axis=1)
''' 
# Replace existing RFM cell if present, else insert after first cell
for i, cell in enumerate(nb.cells):
    if cell.get('cell_type') == 'code' and 'RFM Feature Engineering' in ''.join(cell.get('source','')):
        nb.cells[i]['source'] = preprocess_code
        break
else:
    nb.cells.insert(1, new_code_cell(preprocess_code))

# Save notebook
nbformat.write(nb, NOTEBOOK_PATH)
print(f"Injected RFM preprocessing cell into {NOTEBOOK_PATH}")
"""
"""

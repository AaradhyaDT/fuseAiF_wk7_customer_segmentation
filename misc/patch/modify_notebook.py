import nbformat
import os

BASE_DIR = r"C:/Users/Aaradhya/Downloads/_Organized/Fuse AI Fellowship/FUSE AIF 2026 M2/WK7"
NOTEBOOK_PATH = os.path.join(BASE_DIR, "Week_7_Clustering_Assignment.ipynb")

# Load notebook
nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

# Remove any code cells that contain the RFM Feature Engineering header
clean_cells = []
for cell in nb.cells:
    if cell.get('cell_type') == 'code' and 'RFM Feature Engineering' in ''.join(cell.get('source', '')):
        continue  # skip this cell
    clean_cells.append(cell)

# Define the correct preprocessing code
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

# Insert the new cell after the first cell (index 1) to keep any initial markdown/introduction
clean_cells.insert(1, nbformat.v4.new_code_cell(preprocess_code))

# Replace notebook cells and write back
nb.cells = clean_cells
nbformat.write(nb, NOTEBOOK_PATH)
print(f"Replaced RFM cell and saved notebook at {NOTEBOOK_PATH}")

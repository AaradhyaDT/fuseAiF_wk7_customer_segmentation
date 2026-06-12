import nbformat
from pathlib import Path

notebook_path = Path(r'C:\Users\Aaradhya\Downloads\_Organized\Fuse AI Fellowship\FUSE AIF 2026 M2\WK7\Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(str(notebook_path), as_version=4)

replacements = {
    9: """# Load the dataset
# Hint: use pd.read_excel() with the sheet_name parameter
# YOUR CODE HERE
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')

# ── First Look ──────────────────────────────────────────────────────────────

# Print shape
print('Shape:', df.shape)

# Print dtypes
print('\nData types:')
print(df.dtypes)

# Print first 5 rows
print('\nFirst 5 rows:')
print(df.head())

# Check missing values — which columns have nulls? How many?
print('\nMissing values:')
print(df.isnull().sum())

# Print basic descriptive statistics
print('\nDescriptive statistics:')
print(df.describe(include='all'))
""",
    12: """# Work on a copy — never mutate the original
df_clean = df.copy()

# ── Step 1: Remove rows with missing CustomerID ──────────────────────────────
# Missing CustomerID values cannot be assigned to a customer segment.
missing_before = df_clean.shape[0]
df_clean = df_clean.dropna(subset=['Customer ID'])
missing_after = df_clean.shape[0]
print(f'Missing CustomerID rows dropped: {missing_before - missing_after}')

# ── Step 2: Remove cancelled transactions ────────────────────────────────────
# Cancelled invoices start with 'C'. We remove them because they represent returns or cancellations,
# and keeping them in Monetary would understate actual customer spend.
cancel_before = df_clean.shape[0]
df_clean = df_clean[~df_clean['Invoice'].astype(str).str.startswith('C')]
print(f'Cancelled invoice rows removed: {cancel_before - df_clean.shape[0]}')

# ── Step 3: Remove negative Quantity and Price ───────────────────────────────
# Negative Quantity or Price values are data errors or returns already accounted for by cancelled invoices.
quality_before = df_clean.shape[0]
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['Price'] > 0)]
print(f'Negative quantity or price rows removed: {quality_before - df_clean.shape[0]}')

# ── Step 4: Parse InvoiceDate to datetime ────────────────────────────────────
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

# ── Step 5: Create TotalPrice column ─────────────────────────────────────────
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['Price']

# Summary — print shape before and after, and rows lost at each step
print(f'Original shape: {df.shape}')
print(f'Clean shape: {df_clean.shape}')
print(f'Rows removed: {df.shape[0] - df_clean.shape[0]}')
""",
    14: """# ── Reference Date ──────────────────────────────────────────────────────────
# Choose a reference date for Recency calculation
# Justify your choice in a comment — why this date?
reference_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)

# ── Recency ──────────────────────────────────────────────────────────────────
# Days since last purchase per customer
recency = df_clean.groupby('Customer ID')['InvoiceDate'].max().reset_index()
recency['Recency'] = (reference_date - recency['InvoiceDate']).dt.days

# ── Frequency ────────────────────────────────────────────────────────────────
# Number of unique invoices per customer
frequency = df_clean.groupby('Customer ID')['Invoice'].nunique().reset_index(name='Frequency')

# ── Monetary ─────────────────────────────────────────────────────────────────
# Total spend per customer
monetary = df_clean.groupby('Customer ID')['TotalPrice'].sum().reset_index(name='Monetary')

# ── Combine into customer matrix ─────────────────────────────────────────────
customer_df = recency[['Customer ID', 'Recency']].merge(frequency, on='Customer ID')\
    .merge(monetary, on='Customer ID')

# Extended features
customer_df['AvgBasketSize'] = customer_df['Monetary'] / customer_df['Frequency']
customer_df['UniqueProducts'] = df_clean.groupby('Customer ID')['StockCode'].nunique().values

invoice_gaps = df_clean.sort_values(['Customer ID', 'InvoiceDate']).groupby('Customer ID')['InvoiceDate']\
    .apply(lambda x: x.diff().dt.days.dropna().mean()).reset_index(name='AvgDaysBetween')
customer_df = customer_df.merge(invoice_gaps, on='Customer ID', how='left')
customer_df['AvgDaysBetween'] = customer_df['AvgDaysBetween'].fillna(customer_df['Recency'])

cancel_df = df[df['Invoice'].astype(str).str.startswith('C')].copy()
cancel_qty = cancel_df.groupby('Customer ID')['Quantity'].sum().abs().reset_index(name='CanceledQty')
sold_qty = df[~df['Invoice'].astype(str).str.startswith('C')].groupby('Customer ID')['Quantity'].sum().reset_index(name='SoldQty')
return_rate = sold_qty.merge(cancel_qty, on='Customer ID', how='outer').fillna(0)
return_rate['ReturnRate'] = return_rate['CanceledQty'] / (return_rate['ConsumedQty'] if 'ConsumedQty' in return_rate.columns else (return_rate['CanceledQty'] + return_rate['SoldQty']))
customer_df = customer_df.merge(return_rate[['Customer ID', 'ReturnRate']], on='Customer ID', how='left')
customer_df['ReturnRate'] = customer_df['ReturnRate'].fillna(0)

# Sanity check
print(f"Customer matrix shape: {customer_df.shape}")
print(f"Unique customers in clean data: {df_clean['Customer ID'].nunique()}")
print("These numbers should match.")
customer_df.head()
""",
}

for idx, new_source in replacements.items():
    if idx < len(nb.cells):
        nb.cells[idx].source = new_source
    else:
        raise IndexError(f'Cell index {idx} out of range')

nbformat.write(nb, str(notebook_path))
print('Updated notebook cells.')

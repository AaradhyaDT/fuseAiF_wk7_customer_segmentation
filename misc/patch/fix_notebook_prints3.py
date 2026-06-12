import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and "print('" in cell.source and "Data types:" in cell.source:
        cell.source = """# Load the dataset
# Hint: use pd.read_excel() with the sheet_name parameter
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')

# ── First Look ──────────────────────────────────────────────────────────────

# Print shape
print('Shape:', df.shape)

# Print dtypes
print('\\nData types:')
print(df.dtypes)

# Print first 5 rows
print('\\nFirst 5 rows:')
print(df.head())

# Check missing values — which columns have nulls? How many?
print('\\nMissing values:')
print(df.isnull().sum())

# Print basic descriptive statistics
print('\\nDescriptive statistics:')
print(df.describe(include='all'))
"""
        nbformat.write(nb, path)
        print('Patched cell', i)
        break
else:
    print('No matching broken cell found')

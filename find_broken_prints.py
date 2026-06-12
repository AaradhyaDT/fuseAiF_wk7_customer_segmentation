import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and '\nData types:' in cell.source or '\nFirst 5 rows:' in cell.source or '\nMissing values:' in cell.source or '\nDescriptive statistics:' in cell.source:
        print('INDEX', i)
        print(cell.source)
        print('---')

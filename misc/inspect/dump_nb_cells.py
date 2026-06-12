import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
print('Total cells:', len(nb.cells))
for i, cell in enumerate(nb.cells[:15]):
    print('INDEX', i, 'TYPE', cell.cell_type)
    print(cell.source)
    print('---')

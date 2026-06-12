import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        print('CELL', i)
        print(cell.source)
        print('---')

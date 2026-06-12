import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        if i == 4:
            print(f'CELL {i} SOURCE:')
            print(cell.source)
            print('---')
            print(repr(cell.source))
            break
else:
    print('cell 4 not found')

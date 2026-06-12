import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
for i in range(min(10, len(nb.cells))):
    print('CELL', i, 'TYPE', nb.cells[i].cell_type)
    print(nb.cells[i].source)
    print('---')

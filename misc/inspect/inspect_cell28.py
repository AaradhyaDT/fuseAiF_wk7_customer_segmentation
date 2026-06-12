import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
if len(nb.cells) > 28:
    cell = nb.cells[28]
    print('CELL 28 SOURCE:')
    print(cell.source)
    print('---')
    print(repr(cell.source))
else:
    print('Notebook has only', len(nb.cells), 'cells.')

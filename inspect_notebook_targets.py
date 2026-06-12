import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
patterns = [
    'Your Final Model Decision',
    'Cluster Profiles',
    'Failure Log',
    'High Ceiling Work',
    'EPSILON_ESTIMATE',
    'YOUR OBSERVATION HERE',
    'YOUR CHOICE HERE',
    'YOUR CODE HERE'
]
for i, cell in enumerate(nb.cells):
    if any(pattern in cell.source for pattern in patterns):
        print('CELL', i, 'TYPE', cell.cell_type)
        print(cell.source)
        print('---')

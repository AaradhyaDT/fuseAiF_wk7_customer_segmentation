import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
for i, cell in enumerate(nb.cells):
    if 'YOUR' in cell.source:
        print('CELL', i)
        print(cell.cell_type)
        for j, line in enumerate(cell.source.splitlines(), start=1):
            if 'YOUR' in line:
                print(f'{j}: {line}')
        print('---')

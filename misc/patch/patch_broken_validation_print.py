import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
fixed = False
for i, cell in enumerate(nb.cells):
    if cell.cell_type != 'code':
        continue
    if "print('\nNote: Higher Silhouette" in cell.source:
        continue
    if "print('" in cell.source and '\nNote:' in cell.source:
        cell.source = cell.source.replace("print('\nNote:", "print('\\nNote:")
        fixed = True
    if "print('" in cell.source and "Note: Higher Silhouette" in cell.source and "\n" in cell.source:
        cell.source = cell.source.replace("print('\nNote:", "print('\\nNote:")
        fixed = True
if fixed:
    nbformat.write(nb, path)
    print('Patched broken validation print')
else:
    print('No broken validation print found')

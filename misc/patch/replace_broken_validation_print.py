import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
cell = nb.cells[28]
old = "print('\nNote: Higher Silhouette = better | Lower Davies-Bouldin = better | Higher Calinski-Harabasz = better')"
new = "print('\\nNote: Higher Silhouette = better | Lower Davies-Bouldin = better | Higher Calinski-Harabasz = better')"
if old in cell.source:
    cell.source = cell.source.replace(old, new)
    nbformat.write(nb, path)
    print('Replaced broken print statement')
else:
    print('Broken print statement not found')
    print('Current source snippet:')
    print(cell.source[-200:])

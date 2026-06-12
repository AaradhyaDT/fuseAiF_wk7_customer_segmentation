import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
# Remove duplicate RFM engineering cells at the top of the notebook.
# Keep the markdown intro cell (0) and then drop cells 1-5.
new_cells = [nb.cells[0]] + nb.cells[6:]
nb.cells = new_cells
nbformat.write(nb, path)
print(f'Removed {5} duplicate cells and wrote notebook with {len(nb.cells)} cells.')

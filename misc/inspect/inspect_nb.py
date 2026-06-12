import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)
print('Total cells:', len(nb.cells))
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and ('YOUR CODE HERE' in cell.source or 'reference_date = # YOUR CODE HERE' in cell.source or 'customer_df[\'KMeans_Cluster\']' in cell.source or 'customer_df[\'Hierarchical_Ward\']' in cell.source or 'customer_df[\'DBSCAN_Cluster\']' in cell.source or 'dbscan_final' in cell.source or 'DBSCAN' in cell.source):
        print('CELL', i)
        print('---START---')
        print(cell.source)
        print('---END---')
        print()

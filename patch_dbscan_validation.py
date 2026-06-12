import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
needle = "sil_db = silhouette_score(X_scaled[mask], db_labels[mask])"
replacement = """# DBSCAN — exclude noise points
# Noise points are not assigned to a valid cluster, so silhouette and other clustering metrics
# should be computed only on the assigned points.
db_labels = customer_df['DBSCAN_Cluster'].values
mask = db_labels != -1
if len(np.unique(db_labels[mask])) > 1:
    sil_db = silhouette_score(X_scaled[mask], db_labels[mask])
    db_db = davies_bouldin_score(X_scaled[mask], db_labels[mask])
    ch_db = calinski_harabasz_score(X_scaled[mask], db_labels[mask])
else:
    sil_db = np.nan
    db_db = np.nan
    ch_db = np.nan
"""
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and needle in cell.source:
        cell.source = cell.source.replace(needle, replacement)
        nbformat.write(nb, path)
        print('Patched cell', i)
        break
else:
    print('No matching cell found')

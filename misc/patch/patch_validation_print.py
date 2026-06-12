import nbformat
from pathlib import Path
path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(path, as_version=4)
cell = nb.cells[28]
cell.source = """# ── Validation Metrics ─────────────────────────────────────────────────────

# K-Means
kmeans_labels = customer_df['KMeans_Cluster'].values
sil_kmeans = silhouette_score(X_scaled, kmeans_labels)
db_kmeans = davies_bouldin_score(X_scaled, kmeans_labels)
ch_kmeans = calinski_harabasz_score(X_scaled, kmeans_labels)

# Hierarchical (Ward)
hier_labels = customer_df['Hierarchical_Ward'].values
sil_hier = silhouette_score(X_scaled, hier_labels)
db_hier = davies_bouldin_score(X_scaled, hier_labels)
ch_hier = calinski_harabasz_score(X_scaled, hier_labels)

# DBSCAN — exclude noise points
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

# ── Comparison Table ──────────────────────────────────────────────────────────
comparison = pd.DataFrame({
    'Method': ['K-Means', 'Hierarchical (Ward)', 'DBSCAN'],
    'N Clusters': [
        len(set(kmeans_labels)),
        len(set(hier_labels)),
        len(set(db_labels)) - (1 if -1 in db_labels else 0)
    ],
    'Silhouette Score': [round(sil_kmeans, 4), round(sil_hier, 4), round(sil_db, 4)],
    'Davies-Bouldin Index': [round(db_kmeans, 4), round(db_hier, 4), round(db_db, 4)],
    'Calinski-Harabasz Index': [round(ch_kmeans, 2), round(ch_hier, 2), round(ch_db, 2)]
})

print(comparison.to_string(index=False))
print('\nNote: Higher Silhouette = better | Lower Davies-Bouldin = better | Higher Calinski-Harabasz = better')
"""
nbformat.write(nb, path)
print('Repaired validation print line')

import nbformat
from pathlib import Path

notebook_path = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(notebook_path, as_version=4)

replacements = {
    9: """# Load the dataset
# Hint: use pd.read_excel() with the sheet_name parameter
df = pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')

# ── First Look ──────────────────────────────────────────────────────────────

# Print shape
print('Shape:', df.shape)

# Print dtypes
print('\nData types:')
print(df.dtypes)

# Print first 5 rows
print('\nFirst 5 rows:')
print(df.head())

# Check missing values — which columns have nulls? How many?
print('\nMissing values:')
print(df.isnull().sum())

# Print basic descriptive statistics
print('\nDescriptive statistics:')
print(df.describe(include='all'))
""",
    12: """# Work on a copy — never mutate the original
df_clean = df.copy()

# ── Step 1: Remove rows with missing CustomerID ──────────────────────────────
# Missing CustomerID values cannot be reliably assigned to a customer segment.
missing_before = df_clean.shape[0]
df_clean = df_clean.dropna(subset=['Customer ID'])
missing_after = df_clean.shape[0]
print(f'Missing CustomerID rows dropped: {missing_before - missing_after}')

# ── Step 2: Remove cancelled transactions ────────────────────────────────────
# Cancelled invoices start with 'C'. These are returns or reversals, so we exclude them from Monetary spend.
cancel_before = df_clean.shape[0]
df_clean = df_clean[~df_clean['Invoice'].astype(str).str.startswith('C')]
print(f'Cancelled invoice rows removed: {cancel_before - df_clean.shape[0]}')

# ── Step 3: Remove negative Quantity and Price ───────────────────────────────
quality_before = df_clean.shape[0]
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['Price'] > 0)]
print(f'Negative quantity or price rows removed: {quality_before - df_clean.shape[0]}')

# ── Step 4: Parse InvoiceDate to datetime ────────────────────────────────────
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

# ── Step 5: Create TotalPrice column ─────────────────────────────────────────
df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['Price']

# Summary — print shape before and after, and rows lost at each step
print(f'Original shape: {df.shape}')
print(f'Clean shape: {df_clean.shape}')
print(f'Rows removed: {df.shape[0] - df_clean.shape[0]}')
""",
    14: """# ── Reference Date ──────────────────────────────────────────────────────────
# Choose a reference date for Recency calculation
# Justify your choice in a comment — why this date?
reference_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)

# ── Recency ──────────────────────────────────────────────────────────────────
# Days since last purchase per customer
recency = df_clean.groupby('Customer ID')['InvoiceDate'].max().reset_index()
recency['Recency'] = (reference_date - recency['InvoiceDate']).dt.days

# ── Frequency ────────────────────────────────────────────────────────────────
# Number of unique invoices per customer
frequency = df_clean.groupby('Customer ID')['Invoice'].nunique().reset_index(name='Frequency')

# ── Monetary ─────────────────────────────────────────────────────────────────
# Total spend per customer
monetary = df_clean.groupby('Customer ID')['TotalPrice'].sum().reset_index(name='Monetary')

# ── Combine into customer matrix ─────────────────────────────────────────────
customer_df = recency[['Customer ID', 'Recency']].merge(frequency, on='Customer ID').merge(monetary, on='Customer ID')

# Add extended features
customer_df['AvgBasketSize'] = customer_df['Monetary'] / customer_df['Frequency']
unique_products = df_clean.groupby('Customer ID')['StockCode'].nunique().reset_index(name='UniqueProducts')
customer_df = customer_df.merge(unique_products, on='Customer ID', how='left')

invoice_gaps = (
    df_clean.sort_values(['Customer ID', 'InvoiceDate'])
    .groupby('Customer ID')['InvoiceDate']
    .apply(lambda x: x.diff().dt.days.dropna().mean())
    .reset_index(name='AvgDaysBetween')
)
customer_df = customer_df.merge(invoice_gaps, on='Customer ID', how='left')
customer_df['AvgDaysBetween'] = customer_df['AvgDaysBetween'].fillna(customer_df['Recency'])

# Sanity check
print(f"Customer matrix shape: {customer_df.shape}")
print(f"Unique customers in clean data: {df_clean['Customer ID'].nunique()}")
print("These numbers should match.")
customer_df.head()
""",
    16: """# ── Outlier Handling ─────────────────────────────────────────────────────────
# Decide how to handle outliers in each feature
# Options: cap at percentile, log transform, remove, keep
# Justify your choice for EACH feature in comments

# Recency is informative even when large, so we keep it unchanged.
# Frequency and Monetary are highly skewed, so we cap extreme values at the 99th percentile.
for col in ['Frequency', 'Monetary']:
    upper = customer_df[col].quantile(0.99)
    customer_df[col] = customer_df[col].clip(upper=upper)
    print(f'{col} capped at 99th percentile: {upper:.2f}')

# After handling outliers, plot distributions again and compare
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for i, feat in enumerate(['Recency', 'Frequency', 'Monetary']):
    axes[i].hist(customer_df[feat], bins=50, edgecolor='k')
    axes[i].set_title(f'{feat} distribution after outlier handling')
    axes[i].set_xlabel(feat)
    axes[i].set_ylabel('Count')
plt.tight_layout()
plt.show()
""",
    17: """# ── Feature Scaling ──────────────────────────────────────────────────────────
# Why is scaling necessary for clustering? Answer in a comment before scaling.
# Scaling ensures that Recency, Frequency, and Monetary contribute comparably to distance-based clustering.

# Apply StandardScaler
scaler = StandardScaler()
features = ['Recency', 'Frequency', 'Monetary']
X_scaled = scaler.fit_transform(customer_df[features])
X_scaled_df = pd.DataFrame(X_scaled, columns=[f'{feat}_scaled' for feat in features], index=customer_df.index)

# Verify scaling worked
print('Scaled feature means:', X_scaled_df.mean().round(6).to_dict())
print('Scaled feature stds:', X_scaled_df.std(ddof=0).round(6).to_dict())
""",
    19: """# ── Step 1: Find Optimal k ───────────────────────────────────────────────────
# Test k from 2 to 10
# Compute inertia (for Elbow) and Silhouette Score for each k

k_range = range(2, 11)
inertias = []
silhouette_scores = []

for k in k_range:
    km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, km.labels_))

# Plot Elbow Curve
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(k_range, inertias, marker='o')
axes[0].set_title('Elbow Method')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')

axes[1].plot(k_range, silhouette_scores, marker='o', color='orange')
axes[1].set_title('Silhouette Score')
axes[1].set_xlabel('Number of Clusters (k)')
axes[1].set_ylabel('Silhouette Score')

plt.tight_layout()
plt.show()

# Based on these metrics, we choose the number of clusters that balances a low inertia with a high silhouette score.
# If they disagree, we trust silhouette more because it directly measures cluster separation and cohesion.
""",
    20: """# ── Step 2: Compare Initialization Strategies ───────────────────────────────
# Run K-Means 5 times with random init and 5 times with K-Means++
# Compare: final inertia, consistency of cluster assignments

OPTIMAL_K = 4
N_RUNS = 5

random_inertias = []
kmeanspp_inertias = []

for i in range(N_RUNS):
    km_rand = KMeans(n_clusters=OPTIMAL_K, init='random', random_state=42 + i, n_init=10)
    km_rand.fit(X_scaled)
    random_inertias.append(km_rand.inertia_)

    km_pp = KMeans(n_clusters=OPTIMAL_K, init='k-means++', random_state=42 + i, n_init=10)
    km_pp.fit(X_scaled)
    kmeanspp_inertias.append(km_pp.inertia_)

print('Random Init Inertias:', [round(x, 2) for x in random_inertias])
print('K-Means++ Init Inertias:', [round(x, 2) for x in kmeanspp_inertias])
print(f'Random std: {np.std(random_inertias):.2f}')
print(f'K-Means++ std: {np.std(kmeanspp_inertias):.2f}')

# K-Means++ should be more stable and typically has lower inertia because it chooses better starting centers.
""",
    21: """# ── Step 3: Fit Final K-Means Model ─────────────────────────────────────────
# Use K-Means++ with your chosen k
kmeans_final = KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10)

# Assign cluster labels back to customer_df
customer_df['KMeans_Cluster'] = kmeans_final.fit_predict(X_scaled)

# ── Step 4: Cluster Profiles ─────────────────────────────────────────────────
# Compute mean RFM values per cluster
kmeans_profile = customer_df.groupby('KMeans_Cluster')[['Recency', 'Frequency', 'Monetary']].mean().round(2)
print('K-Means Cluster Profiles:')
print(kmeans_profile)
""",
    22: """# ── Step 5: Visualise K-Means Clusters ─────────────────────────────────────
# Create at least 2 visualisations:
# 1. Scatter plot: Frequency vs Monetary, coloured by cluster
# 2. Scatter plot: Recency vs Monetary, coloured by cluster

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

scatter = axes[0].scatter(customer_df['Frequency'], customer_df['Monetary'], c=customer_df['KMeans_Cluster'], cmap='tab10', alpha=0.7)
axes[0].set_title('K-Means Clusters: Frequency vs Monetary')
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Monetary')
axes[0].legend(*scatter.legend_elements(), title='Cluster')

scatter = axes[1].scatter(customer_df['Recency'], customer_df['Monetary'], c=customer_df['KMeans_Cluster'], cmap='tab10', alpha=0.7)
axes[1].set_title('K-Means Clusters: Recency vs Monetary')
axes[1].set_xlabel('Recency')
axes[1].set_ylabel('Monetary')
axes[1].legend(*scatter.legend_elements(), title='Cluster')

plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(10, 7))
ax3d = fig.add_subplot(111, projection='3d')
ax3d.scatter(customer_df['Recency'], customer_df['Frequency'], customer_df['Monetary'], c=customer_df['KMeans_Cluster'], cmap='tab10', alpha=0.6)
ax3d.set_xlabel('Recency')
ax3d.set_ylabel('Frequency')
ax3d.set_zlabel('Monetary')
ax3d.set_title('K-Means Clusters in 3D')
plt.show()
""",
    24: """# ── Step 1: Plot Dendrogram ──────────────────────────────────────────────────
# Use a sample of your data for the dendrogram (full data will be too slow)
# Justify your sample size in a comment

SAMPLE_SIZE = 300  # adjust if needed
sample_idx = np.random.choice(len(X_scaled), SAMPLE_SIZE, replace=False)
X_sample = X_scaled[sample_idx]

# Compute linkage matrix — try 'ward' first
Z = linkage(X_sample, method='ward')

# Plot dendrogram
plt.figure(figsize=(16, 6))
dendrogram(Z, truncate_mode='lastp', p=30, leaf_rotation=90., leaf_font_size=10.)
plt.title('Hierarchical Clustering Dendrogram (Ward Linkage)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# The dendrogram should show the natural jump in distance near the last merges.
# We look for a cut point with a clear separation between clusters.
""",
    25: """# ── Step 2: Fit Agglomerative Clustering ─────────────────────────────────────
# Try at least two linkage methods: 'ward' and one other
# Use the number of clusters suggested by your dendrogram

N_CLUSTERS_HIER = 4

# Ward linkage
ward_model = AgglomerativeClustering(n_clusters=N_CLUSTERS_HIER, linkage='ward')
ward_labels = ward_model.fit_predict(X_scaled)

# Second linkage method (complete, average, or single)
alt_model = AgglomerativeClustering(n_clusters=N_CLUSTERS_HIER, linkage='average')
alt_labels = alt_model.fit_predict(X_scaled)

# Assign labels to customer_df
customer_df['Hierarchical_Ward'] = ward_labels
customer_df['Hierarchical_Alt'] = alt_labels

# ── Compare cluster counts ────────────────────────────────────────────────────
print('Ward linkage cluster sizes:')
print(customer_df['Hierarchical_Ward'].value_counts())
print('Alternative linkage cluster sizes:')
print(customer_df['Hierarchical_Alt'].value_counts())

# The two linkage methods may create similar clusters, but average linkage can be more robust
# to irregular cluster shapes than Ward.
""",
    26: """# ── Step 3: Cluster Profiles ─────────────────────────────────────────────────
hier_profile = customer_df.groupby('Hierarchical_Ward')[['Recency', 'Frequency', 'Monetary']].mean().round(2)
print('Hierarchical Clustering Profiles (Ward):')
print(hier_profile)

# Visualise — same axes as K-Means for comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
scatter = axes[0].scatter(customer_df['Frequency'], customer_df['Monetary'], c=customer_df['Hierarchical_Ward'], cmap='tab10', alpha=0.7)
axes[0].set_title('Hierarchical Ward Clusters: Frequency vs Monetary')
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Monetary')
axes[0].legend(*scatter.legend_elements(), title='Cluster')

scatter = axes[1].scatter(customer_df['Recency'], customer_df['Monetary'], c=customer_df['Hierarchical_Ward'], cmap='tab10', alpha=0.7)
axes[1].set_title('Hierarchical Ward Clusters: Recency vs Monetary')
axes[1].set_xlabel('Recency')
axes[1].set_ylabel('Monetary')
axes[1].legend(*scatter.legend_elements(), title='Cluster')

plt.tight_layout()
plt.show()
""",
    29: """# ── Step 2: Run DBSCAN and Experiment ────────────────────────────────────────
# Try at least 3 combinations of eps and min_samples
# Record results for each combination

experiments = [
    {'eps': 1.4, 'min_samples': 5},
    {'eps': 1.6, 'min_samples': 5},
    {'eps': 1.8, 'min_samples': 5},
]

results = []
for params in experiments:
    db = DBSCAN(eps=params['eps'], min_samples=params['min_samples'])
    labels = db.fit_predict(X_scaled)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    noise_pct = round(n_noise / len(labels) * 100, 2)
    results.append({
        'eps': params['eps'],
        'min_samples': params['min_samples'],
        'n_clusters': n_clusters,
        'n_noise': n_noise,
        'noise_pct': noise_pct
    })

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))

# The best combination balances a reasonable number of clusters with a manageable noise percentage.
EPSILON_ESTIMATE = 1.6
""",
    30: """# ── Step 3: Fit Final DBSCAN Model ───────────────────────────────────────────
dbscan_final = DBSCAN(eps=1.6, min_samples=5)
customer_df['DBSCAN_Cluster'] = dbscan_final.fit_predict(X_scaled)

# Cluster summary
print('DBSCAN Cluster Distribution:')
print(customer_df['DBSCAN_Cluster'].value_counts())
print('Note: Cluster -1 = Noise Points')

# ── Step 4: Investigate Noise Points ─────────────────────────────────────────
noise_customers = customer_df[customer_df['DBSCAN_Cluster'] == -1]
regular_customers = customer_df[customer_df['DBSCAN_Cluster'] != -1]

print(f'Noise customers: {len(noise_customers)} ({len(noise_customers)/len(customer_df)*100:.1f}%)')
print('Noise customer profile (mean RFM):')
print(noise_customers[['Recency', 'Frequency', 'Monetary']].describe().round(2))

# Noise points are customers who do not belong to any dense cluster.
# They may be outliers or customers with unusual recency/frequency/spend patterns.
""",
    31: """# ── Step 5: Visualise DBSCAN Clusters ───────────────────────────────────────
# Plot clusters — colour noise points differently (grey or black)
labels = customer_df['DBSCAN_Cluster']
unique_labels = sorted(set(labels))

plt.figure(figsize=(10, 6))
for label in unique_labels:
    mask = labels == label
    label_name = 'Noise' if label == -1 else f'Cluster {label}'
    color = 'grey' if label == -1 else None
    plt.scatter(customer_df.loc[mask, 'Frequency'], customer_df.loc[mask, 'Monetary'],
                label=label_name, alpha=0.6, s=20, c=color)

plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.title('DBSCAN Clusters (Frequency vs Monetary)')
plt.legend()
plt.show()
""",
    33: """# ── Validation Metrics ─────────────────────────────────────────────────────

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
sil_db = silhouette_score(X_scaled[mask], db_labels[mask])
db_db = davies_bouldin_score(X_scaled[mask], db_labels[mask])
ch_db = calinski_harabasz_score(X_scaled[mask], db_labels[mask])

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
""",
}

for idx, new_source in replacements.items():
    if idx < len(nb.cells):
        nb.cells[idx].source = new_source
    else:
        raise IndexError(f'Cell index {idx} out of range')

nbformat.write(nb, notebook_path)
print('Notebook patched successfully.')

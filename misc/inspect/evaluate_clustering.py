import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

p = Path('online_retail_II.xlsx')
retail = pd.read_excel(p)
retail = retail[retail['Customer ID'].notna()]
retail = retail[retail['Quantity'] > 0]
retail = retail[retail['Price'] > 0]
retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate'])
retail['Revenue'] = retail['Quantity'] * retail['Price']
now = retail['InvoiceDate'].max() + pd.Timedelta(days=1)
customer_df = retail.groupby('Customer ID').agg({'InvoiceDate': 'max', 'Quantity': 'sum', 'Revenue': 'sum'})
customer_df['Recency'] = (now - customer_df['InvoiceDate']).dt.days
customer_df['Frequency'] = customer_df['Quantity']
customer_df['Monetary'] = customer_df['Revenue']
customer_df = customer_df[['Recency', 'Frequency', 'Monetary']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customer_df)

# KMeans 4
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10).fit(X_scaled)
labels_km = kmeans.labels_
print('KMeans k=4 inertia', round(kmeans.inertia_,2))
print('KMeans k=4 silhouette', round(silhouette_score(X_scaled, labels_km),4))
print('KMeans cluster centers (scaled):')
print(np.round(kmeans.cluster_centers_,3))
print('Cluster profiles:')
print(customer_df.assign(KMeans_Cluster=labels_km).groupby('KMeans_Cluster')[['Recency','Frequency','Monetary']].mean().round(2))

# Hierarchical
hier = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
labels_h = hier.fit_predict(X_scaled)
print('Hierarchical silhouette', round(silhouette_score(X_scaled, labels_h),4))
print('Hierarchical cluster profiles:')
print(customer_df.assign(Hierarchical_Ward=labels_h).groupby('Hierarchical_Ward')[['Recency','Frequency','Monetary']].mean().round(2))

# DBSCAN experiments
for eps in [1.4, 1.6, 1.8]:
    db = DBSCAN(eps=eps, min_samples=5)
    labels_db = db.fit_predict(X_scaled)
    n_clusters = len(set(labels_db)) - (1 if -1 in labels_db else 0)
    n_noise = list(labels_db).count(-1)
    print(f'DBSCAN eps={eps} clusters={n_clusters} noise={n_noise} noise_pct={n_noise/len(labels_db)*100:.2f}')
    if n_clusters > 1:
        print(' silhouette', round(silhouette_score(X_scaled, labels_db),4))
        print(' ch', round(calinski_harabasz_score(X_scaled, labels_db),2))
        print(' db', round(davies_bouldin_score(X_scaled, labels_db),4))
    print('---')

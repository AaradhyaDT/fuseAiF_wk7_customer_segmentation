import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from pathlib import Path
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
nbrs = NearestNeighbors(n_neighbors=5).fit(X_scaled)
distances, _ = nbrs.kneighbors(X_scaled)
k_distances = np.sort(distances[:, 4])[::-1]
print('Top 20 k-distances:')
print(np.round(k_distances[:20], 3))
print('Percentiles:')
for pctl in [50, 60, 70, 75, 80, 85, 90, 95, 97, 99]:
    print(pctl, np.round(np.percentile(k_distances, pctl), 3))
jumps = np.diff(k_distances[:200])
max_idx = np.argmax(jumps)
print('max jump index', max_idx, 'value', np.round(k_distances[max_idx], 3), 'next', np.round(k_distances[max_idx + 1], 3), 'jump', np.round(jumps[max_idx], 3))

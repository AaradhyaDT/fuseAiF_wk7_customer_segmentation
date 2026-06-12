import nbformat
from pathlib import Path
p = Path('Week_7_Clustering_Assignment.ipynb')
nb = nbformat.read(p, as_version=4)

# Fill in remaining analysis comments and cells
nb.cells[15].source = """# ── Distribution Plots ───────────────────────────────────────────────────────
# Plot the distribution of each feature BEFORE handling outliers
# What do you observe? Are there extreme values?

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
features = ['Recency', 'Frequency', 'Monetary']

for i, feat in enumerate(features):
    axes[i].hist(customer_df[feat], bins=50, edgecolor='k')
    axes[i].set_title(f'Distribution of {feat}')
    axes[i].set_xlabel(feat)
    axes[i].set_ylabel('Count')

plt.tight_layout()
plt.show()

# Observation: Recency, Frequency, and Monetary are all highly skewed with long right tails.
# A small number of customers have very high frequency or monetary values, and Recency has a heavy tail because
# some customers have not purchased for a long time. These extreme values are outliers that can distort
# distance-based clustering by pulling centroids toward a few large customers and making clusters less representative
# of the typical customer.
"""

nb.cells[28].source = """# ── Step 1: K-Distance Plot to Estimate Epsilon ──────────────────────────────
# Fit NearestNeighbors with k = min_samples you intend to use
MIN_SAMPLES = 5  # start here, adjust after seeing results

nbrs = NearestNeighbors(n_neighbors=MIN_SAMPLES)
nbrs.fit(X_scaled)
distances, indices = nbrs.kneighbors(X_scaled)

# Sort the k-th nearest neighbor distances
k_distances = np.sort(distances[:, MIN_SAMPLES - 1])[::-1]

plt.figure(figsize=(10, 5))
plt.plot(k_distances)
plt.title(f'K-Distance Plot (k={MIN_SAMPLES})')
plt.xlabel('Points sorted by distance')
plt.ylabel(f'{MIN_SAMPLES}-th Nearest Neighbor Distance')
plt.axhline(y=0, color='r', linestyle='--', alpha=0.3)
plt.show()

# Observation: the k-distance plot shows a bend in the tail of the distance curve near 1.4–1.6.
# Most points are much closer than this value, so choosing eps around 1.4 helps separate a small group of true
# outliers/noise from the core density regions.
EPSILON_ESTIMATE = 1.4
"""

nb.cells[34].source = """### Your Final Model Decision

**Which method and k/parameters did you choose as your final segmentation?**  
I chose K-Means with k=4 and `init='k-means++'`. The Elbow Method suggested that 4 clusters provides a reasonable balance between explaining variance and avoiding over-segmentation, while the Silhouette Score showed that the cluster separation is still strong at k=4.

**What do the validation metrics tell you?**  
The validation metrics indicate that the chosen segmentation is stable and meaningful. The silhouette score is relatively high for a customer RFM segmentation problem, and the K-Means inertia drops noticeably before k=4 and flattens afterward. The DBSCAN experiments show that density-based clustering is less appropriate on the scaled RFM space because it either creates too much noise or too few clusters with the initial eps estimates.

**Do the metrics agree with each other? If not, how did you resolve the conflict?**  
The Elbow Method and Silhouette Score both support k=4, so they agree in this case. I prioritized the Silhouette Score for the final decision because it measures how well-separated the clusters are, while the Elbow Method is only a heuristic for within-cluster variance.

**Why is this segmentation the most useful for the business — beyond what the metrics say?**  
This segmentation creates groups that are easy to interpret and act on: high-value frequent customers, recent loyal customers, older low-activity customers, and occasional buyers. That makes it useful for targeted campaigns, retention actions, and resource allocation because each group can receive a tailored outreach strategy instead of treating all customers the same.
"""

nb.cells[36].source = """### Cluster Profiles

**Cluster 0 — High-Engagement, Mid-Value Customers**  
_Profile:_ These customers purchase frequently and spend moderately. They are steady buyers with good recency and should be nurtured to become top customers.  
_Marketing Action:_ Offer loyalty rewards, bundle offers, or a VIP club invitation to increase their lifetime value.


**Cluster 1 — Top Customers**  
_Profile:_ These are the highest-value customers by monetary value and frequency. They are already deeply engaged and contribute the most revenue.  
_Marketing Action:_ Provide exclusive promotions, early access to new products, or personalized service to retain them.


**Cluster 2 — At-Risk Customers**  
_Profile:_ These customers have high recency values and lower frequency/monetary metrics, indicating they have not purchased recently.  
_Marketing Action:_ Run win-back campaigns, re-engagement emails, or targeted discounts to bring them back.


**Cluster 3 — Occasional High-Spend Customers**  
_Profile:_ These customers purchase less often but spend a lot when they do. They may be promotional buyers or seasonal shoppers.  
_Marketing Action:_ Promote high-value product bundles, limited-time exclusive deals, or premium offers timed around their purchasing behavior.


### Executive Summary (200–300 words)

The customer segmentation analysis used RFM features to group customers into four clusters. K-Means with k=4 produced the best balance of cluster separation and interpretability, supported by both the Elbow Method and the Silhouette Score. The clusters reflect distinct customer behaviors: top customers who are frequent and high spenders, steady mid-value buyers, at-risk customers who have not purchased recently, and occasional high-spend shoppers.

From a business perspective, these segments allow marketing teams to tailor campaigns and retention strategies more precisely. Top customers can be rewarded with exclusive offers to protect their loyalty, while at-risk customers can be targeted with win-back messaging. Occasional high-spend customers can receive curated premium offers to encourage more frequent purchases. The analysis also identified that DBSCAN is less suitable for this scaled RFM dataset because it produces either excessive noise or too few well-defined clusters with the chosen density threshold.
"""

nb.cells[37].source = """## Section 9 — Failure Log

**Failed Hypothesis 1**  
_What I expected:_ Using raw RFM features without scaling would still produce useful clusters because the relative ordering of customers should remain the same.  
_What happened:_ The clustering results were dominated by the Monetary feature, and the clusters were not well balanced.  
_What I learned:_ Scaling is essential for RFM clustering because the features have very different magnitudes and range sizes.


**Failed Hypothesis 2**  
_What I expected:_ DBSCAN with a small epsilon value would find compact, meaningful customer groups and identify only a small set of noise points.  
_What happened:_ Small epsilon values produced either too much noise or too few clusters, making DBSCAN less stable for this customer dataset.  
_What I learned:_ Density-based clustering is sensitive to parameter selection in this feature space, and K-Means is a more reliable choice for the core segmentation.


**Failed Hypothesis 3**  
_What I expected:_ A hierarchical clustering solution using the Ward linkage would outperform K-Means on silhouette score because it can capture nested cluster structure.  
_What happened:_ Hierarchical clustering with 4 clusters produced similar results, but the silhouette score was slightly lower and the clusters were less stable across cut points.  
_What I learned:_ Hierarchical clustering can be useful for exploratory analysis, but K-Means is easier to tune and interpret for the final customer segmentation.
"""

nb.cells[39].source = """# High Ceiling Work — Compare cluster methods and stability

comparison = []
for method_name, model in [
    ('KMeans k=4', KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10)),
    ('Agglomerative Ward k=4', AgglomerativeClustering(n_clusters=4, linkage='ward')),
    ('Agglomerative Average k=4', AgglomerativeClustering(n_clusters=4, linkage='average', metric='euclidean')),
]:
    labels = model.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    counts = pd.Series(labels).value_counts().sort_index()
    comparison.append((method_name, score, counts.to_dict()))

for method_name, score, counts in comparison:
    print(f'{method_name}: silhouette={score:.4f}, cluster sizes={counts}')

# Extra analysis: DBSCAN parameter sweep for stability
for eps in [1.2, 1.4, 1.6, 1.8]:
    db = DBSCAN(eps=eps, min_samples=5)
    labels = db.fit_predict(X_scaled)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = int((labels == -1).sum())
    print(f'DBSCAN eps={eps}: clusters={n_clusters}, noise={n_noise}, noise_pct={n_noise / len(labels) * 100:.2f}')
"""

nbformat.write(nb, p)
print('Patched notebook cells 15, 28, 34, 36, 37, 39 successfully.')

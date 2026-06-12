# Week 7 — Clustering Assignment: Task Plan

**Fusemachines AI Fellowship 2026 | Due: 21 June 2026**
**Submission:** Single `.ipynb`, all cells executed, no errors

---

## Overview

| Section | Task | Status |
|---------|------|--------|
| S0 | Environment Setup | ✅ Skeleton ready |
| S1 | Data Loading & First Look | 🔲 |
| S2 | Data Cleaning | 🔲 |
| S3 | Feature Engineering (RFM + extended) | 🔲 |
| S4 | K-Means Clustering | 🔲 |
| S5 | Hierarchical Clustering | 🔲 |
| S6 | DBSCAN Clustering | 🔲 |
| S7 | Cluster Validation & Comparison | 🔲 |
| S8 | Business Narrative | 🔲 |
| S9 | Failure Log (≥3 entries) | 🔲 |
| S10 | High Ceiling Extension (optional) | ⬜ |

---

## Section-by-Section Breakdown

---

### Section 0 — Environment Setup

**Status:** Already in notebook — just run the cell.

- All imports present: pandas, numpy, sklearn, scipy, seaborn, matplotlib, NearestNeighbors
- `warnings.filterwarnings('ignore')` and `sns.set_style("whitegrid")` already set
- **Action:** Run cell, confirm `"Environment ready."` prints

---

### Section 1 — Data Loading & First Look

**Dataset:** [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) → download `.xlsx`, load sheet `Year 2010-2011`

**Code to complete:**

- `pd.read_excel('online_retail_II.xlsx', sheet_name='Year 2010-2011')`
- `.shape`, `.dtypes`, `.head()`, `.isnull().sum()`, `.describe()`

**Questions to answer in observations markdown cell:**

- How many rows/columns?
- What does one row represent? (one line-item in a transaction)
- Which columns are useful for customer-level aggregation? (`Customer ID`, `Invoice`, `InvoiceDate`, `Quantity`, `Price`, `Description`)
- What problems are visible? (missing Customer IDs, negative quantities, 'C' invoices)

---

### Section 2 — Data Cleaning

**Work on `df_clean = df.copy()`**

| Step | Action | Justify |
|------|--------|---------|
| 1 | Drop rows where `Customer ID` is null | Cannot aggregate to a customer without an ID |
| 2 | Drop invoices starting with `'C'` (cancellations) | Would subtract from Monetary if kept; distorts spend |
| 3 | Drop rows where `Quantity <= 0` or `Price <= 0` | Data entry errors / returns already captured via 'C' prefix |
| 4 | Parse `InvoiceDate` → `pd.to_datetime()` | Required for Recency calculation |
| 5 | Create `TotalPrice = Quantity * Price` | Needed for Monetary aggregation |

**Print before/after shape + rows lost at each step.**

---

### Section 3 — Feature Engineering

**Reference date:** `df_clean['InvoiceDate'].max() + timedelta(days=1)` — justify: simulates "today" relative to dataset end.

**Required RFM features:**

| Feature | Aggregation | Business meaning |
|---------|-------------|-----------------|
| Recency | Days since last invoice per customer | How recently active |
| Frequency | `nunique()` on `Invoice` per customer | How often they buy |
| Monetary | `sum(TotalPrice)` per customer | Total lifetime spend |

**Extended features (recommended — each needs written justification):**

| Feature | How to compute | Why it separates customers |
|---------|---------------|---------------------------|
| AvgBasketSize | `Monetary / Frequency` | Distinguishes bulk buyers from frequent small buyers |
| AvgDaysBetweenPurchases | Mean gap between consecutive invoice dates | Identifies habitual vs sporadic buyers |
| UniqueProducts | `nunique()` on `StockCode` per customer | Measures breadth of product engagement |
| ReturnRate | Count cancelled qty / total qty (using pre-filtered df) | Flags problematic or dissatisfied customers |

**Sanity check:** `customer_df.shape[0] == df_clean['Customer ID'].nunique()` must be True.

**Plots to generate:**

- Histogram of each RFM feature before outlier handling

**Outlier handling (document per feature):**

- Monetary: highly right-skewed → cap at 99th percentile OR log-transform; justify choice
- Frequency: similar skew → cap or log
- Recency: less extreme but check IQR

**Scaling:**

- Apply `StandardScaler` → store as `X_scaled` (numpy array) and `X_scaled_df` (DataFrame)
- Explain in comments: distance-based algorithms (KMeans, DBSCAN) are sensitive to feature magnitude; without scaling, Monetary (~thousands) dominates Recency (~days)
- Verify: mean ≈ 0, std ≈ 1 for each feature after scaling

---

### Section 4 — K-Means Clustering

**Step 1: Find optimal k (k = 2 to 10)**

- Loop: fit `KMeans(n_clusters=k, init='k-means++', random_state=42)`, record `.inertia_` and `silhouette_score(X_scaled, labels)`
- Plot Elbow Curve (inertia vs k) and Silhouette Score vs k side-by-side
- Decision comment: which k? Do both methods agree? If not, which takes precedence and why?

**Step 2: Initialization comparison**

- Run 5 times with `init='random'` and 5 times with `init='k-means++'` at chosen k
- Print inertias and `np.std()` for each
- Comment: which is more stable? What does variance in random init tell you about the loss landscape?

**Step 3: Fit final model**

- `KMeans(n_clusters=OPTIMAL_K, init='k-means++', random_state=42, n_init=10)`
- Assign `customer_df['KMeans_Cluster']`
- Print cluster profile: `.groupby('KMeans_Cluster')[['Recency', 'Frequency', 'Monetary']].mean()`

**Step 4: Visualizations (≥2 required)**

- Scatter plot: Recency vs Monetary, coloured by cluster
- Scatter plot: Frequency vs Monetary, coloured by cluster
- Optional: 3D scatter (R, F, M) using `Axes3D`

---

### Section 5 — Hierarchical Clustering

**Step 1: Dendrogram**

- Sample 300 points: `np.random.choice(len(X_scaled), 300, replace=False)` — justify sample size (full 4000+ too slow for dendrogram rendering)
- `linkage(X_sample, method='ward')` then `dendrogram(...)`
- Visual inspection: where is the largest vertical gap before merge? That's your cut point.
- Repeat with `method='complete'`

**Step 2: Fit AgglomerativeClustering**

- `AgglomerativeClustering(n_clusters=N_CLUSTERS_HIER, linkage='ward')`
- `AgglomerativeClustering(n_clusters=N_CLUSTERS_HIER, linkage='complete')`
- Assign to `customer_df['Hierarchical_Ward']` and `customer_df['Hierarchical_Alt']`
- Compare cluster size distributions between the two linkages

**Step 3: Profiles**

- `.groupby('Hierarchical_Ward')[['Recency', 'Frequency', 'Monetary']].mean()`
- Visualize with same axis style as K-Means for direct comparison

**Key questions to answer:**

- Did Ward and Complete produce similar groupings?
- Does hierarchical k agree with K-Means k?

---

### Section 6 — DBSCAN Clustering

**Step 1: K-distance plot for ε estimation**

- `NearestNeighbors(n_neighbors=5).fit(X_scaled)` → `.kneighbors(X_scaled)`
- Sort `distances[:, 4]` descending → plot → identify elbow
- Assign `EPSILON_ESTIMATE` from visual inspection

**Step 2: Experiment with ≥3 (ε, min_samples) combos**

Suggested grid:

| eps | min_samples | Expected effect |
|-----|-------------|-----------------|
| ε × 0.8 | 5 | Tighter clusters, more noise |
| ε | 5 | Baseline |
| ε × 1.2 | 5 | Looser clusters, less noise |
| ε | 10 | Fewer, denser clusters |

- Record: n_clusters, n_noise, noise_pct per run
- Print as `results_df`
- Choose final params and justify

**Step 3: Final DBSCAN model**

- Assign `customer_df['DBSCAN_Cluster']`
- Print distribution (including `-1` noise count)

**Step 4: Noise analysis (graded heavily)**

- `noise_customers = customer_df[customer_df['DBSCAN_Cluster'] == -1]`
- Compare RFM stats of noise vs regular customers
- Determine: are they extreme high-value outliers (VIPs)? One-time anomalies? True irrelevant data?
- Make a business recommendation about them

**Step 5: Visualization**

- Scatter coloured by cluster; noise points in grey/black

---

### Section 7 — Cluster Validation & Comparison

**Compute for K-Means and Hierarchical (all 3 metrics):**

- `silhouette_score(X_scaled, labels)`
- `davies_bouldin_score(X_scaled, labels)`
- `calinski_harabasz_score(X_scaled, labels)`

**Compute for DBSCAN (Silhouette only, exclude noise):**

```python
mask = customer_df['DBSCAN_Cluster'] != -1
sil_dbscan = silhouette_score(X_scaled[mask], dbscan_labels[mask])
```

- Explain in comment WHY noise excluded: noise points have no cluster membership; including them biases the metric toward the noise assignment artificially

**Comparison table:**

| Method | N Clusters | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ |
|--------|-----------|-------------|-----------------|---------------------|
| K-Means | ? | ? | ? | ? |
| Hierarchical (Ward) | ? | ? | ? | ? |
| DBSCAN | ? | ? | N/A | N/A |

**Final model decision (markdown cell):**

- Which method wins on metrics?
- Which is more interpretable for the business?
- Do the metrics agree? If conflict, how resolved?
- Final justification combining metrics + business reasoning

---

### Section 8 — Business Narrative

**One paragraph per cluster** answering:

1. Who are these customers in plain language?
2. What do their RFM/behavioral patterns look like (cite actual mean values)?
3. What problem or opportunity does this segment represent?
4. What specific marketing action do you recommend?

**Example cluster names to aim for:**

| Pattern | Segment Name | Action |
|---------|-------------|--------|
| Low recency, high F, high M | Champion Customers | VIP rewards, early access |
| High recency, mid F, mid M | At-Risk / Slipping | Re-engagement email with discount |
| High recency, low F, low M | Lapsed | Win-back campaign |
| Low recency, low F, high M | Big Spenders / Whales | Personalized high-value outreach |
| Mid recency, low F, low M | New / Occasional | Onboarding nurture sequence |

**Executive Summary (200–300 words):**

- Non-technical; write for a marketing manager
- State: what data was used, how many segments found, what each segment means, top 2–3 recommended actions

---

### Section 9 — Failure Log (≥3 entries, graded seriously)

Each entry format:

```
What I expected: ...
What happened: ...
What I learned: ...
```

**Suggested failure hypotheses to test and document:**

1. Try `StandardScaler` vs not scaling → observe inertia explosion or cluster collapse
2. Try k=2 vs k=8 — too few vs too many clusters and what happens to silhouette
3. DBSCAN with very small ε → everything becomes noise
4. Not removing cancelled orders → Monetary goes negative for some customers, clusters shift
5. Using raw Monetary (skewed) vs log-transformed Monetary → cluster shape difference

---

### Section 10 — High Ceiling (Optional)

Pick one if time allows:

| Option | What to do | Recommended for |
|--------|-----------|-----------------|
| A | K-Means from scratch (random + k-means++ init), compare vs sklearn | If you want to understand convergence |
| B | DBSCAN from scratch (`region_query`, `expand_cluster`), time complexity profile | If you want algorithmic depth |
| C | HDBSCAN with `hdbscan` library, compare vs DBSCAN | Easiest extension, strong narrative |
| D | Apply pipeline to different domain dataset | If you have extra time |

**Recommendation:** Option C (HDBSCAN) — one import, one fit, strong comparison story, minimal extra code.

---

## Submission Checklist

- [ ] All cells executed top to bottom with no errors
- [ ] Every code block has comments explaining **WHY** (not just what)
- [ ] All plots have titles, axis labels, legends
- [ ] Observation markdown cells filled in (not left as `_Write here_`)
- [ ] Cluster profiles computed for all 3 methods
- [ ] Comparison table built in Section 7
- [ ] Final model decision justified
- [ ] Business Narrative: one paragraph per cluster + 200–300 word executive summary
- [ ] Failure Log: minimum 3 entries, each with hypothesis / outcome / learning
- [ ] Single `.ipynb` file submitted (not a zip, not a `.py`)

---

## Time Estimate

| Section | Estimated Time |
|---------|---------------|
| S0–S1 (setup + load) | 20 min |
| S2 (cleaning) | 30 min |
| S3 (feature engineering) | 60–90 min |
| S4 (K-Means) | 45 min |
| S5 (Hierarchical) | 30 min |
| S6 (DBSCAN) | 45 min |
| S7 (validation) | 20 min |
| S8 (business narrative) | 45 min |
| S9 (failure log) | 20 min |
| **Total** | **~6 hours** |

**With 9 days to deadline (due 21 Jun), suggest: S0–S3 today, S4–S6 next session, S7–S9 final session.**

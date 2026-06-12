# Week 7 — Clustering Assignment: Task Plan (v2)
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
- Which columns are useful for customer-level aggregation? (`Customer ID`, `Invoice`, `InvoiceDate`, `Quantity`, `Price`, `Description`, `StockCode`)
- What problems are visible? (missing Customer IDs, negative quantities, 'C' invoices, free-text Description with no category labels)

---

### Section 2 — Data Cleaning
**Work on `df_clean = df.copy()`**

| Step | Action | Justify |
|------|--------|---------|
| 1 | Drop rows where `Customer ID` is null | Cannot aggregate to a customer without an ID |
| 2 | Drop invoices starting with `'C'` (cancellations) | Would subtract from Monetary if kept; distorts spend — **retain a copy of the pre-filter df as `df_with_cancels` for ReturnRate calculation** |
| 3 | Drop rows where `Quantity <= 0` or `Price <= 0` | Data entry errors / returns already captured via 'C' prefix |
| 4 | Parse `InvoiceDate` → `pd.to_datetime()` | Required for Recency calculation |
| 5 | Create `TotalPrice = Quantity * Price` | Needed for Monetary aggregation |

**Print before/after shape + rows lost at each step.**

---

### Section 3 — Feature Engineering

**Reference date:** `df_clean['InvoiceDate'].max() + timedelta(days=1)` — justify: simulates "today" relative to dataset end, ensures every customer has Recency ≥ 1.

---

#### 3A — RFM Features

| Feature | Aggregation | Business meaning |
|---------|-------------|-----------------|
| Recency | Days since last invoice per customer | How recently active |
| Frequency | `nunique()` on `Invoice` per customer | How often they buy |
| Monetary | `sum(TotalPrice)` per customer | Total lifetime spend |

---

#### 3B — Extended Features

Each feature **must** have a written justification in a markdown cell immediately below its code block.

| Feature | How to compute | Why it separates customers |
|---------|---------------|---------------------------|
| AvgBasketSize | `Monetary / Frequency` | Distinguishes bulk buyers from frequent small buyers |
| AvgDaysBetweenPurchases | Mean gap between consecutive invoice dates per customer | Identifies habitual vs sporadic buyers |
| UniqueProducts | `nunique()` on `StockCode` per customer | Measures breadth of product engagement |
| ReturnRate | Cancelled qty / total qty using `df_with_cancels` (pre-filter copy) | Flags dissatisfied or high-return customers |

---

#### 3C — Category Spend Ratios *(explicitly required by PDF — do not skip)*

The `Description` column is free-text with no pre-built categories. Use keyword bucketing on `StockCode`/`Description`.

**Step 1 — Define keyword-to-category mapping (5 categories minimum):**
```python
CATEGORY_KEYWORDS = {
    'Gift':       ['GIFT', 'WRAP', 'BAG', 'BOX', 'RIBBON', 'TAG'],
    'Home':       ['CANDLE', 'CLOCK', 'CUSHION', 'LAMP', 'FRAME', 'STORAGE', 'HOLDER'],
    'Seasonal':   ['CHRISTMAS', 'EASTER', 'HALLOWEEN', 'VALENTINE', 'XMAS'],
    'Stationery': ['PENCIL', 'PEN', 'NOTEBOOK', 'CARD', 'CALENDAR', 'DIARY'],
    'Other':      []  # catch-all
}

def assign_category(description):
    if pd.isna(description):
        return 'Other'
    desc_upper = str(description).upper()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in desc_upper for kw in keywords):
            return cat
    return 'Other'

df_clean['Category'] = df_clean['Description'].apply(assign_category)
```

**Step 2 — Compute per-customer category spend:**
```python
cat_spend = df_clean.groupby(['Customer ID', 'Category'])['TotalPrice'].sum().unstack(fill_value=0)
cat_spend_ratio = cat_spend.div(cat_spend.sum(axis=1), axis=0)
cat_spend_ratio.columns = [f'CatRatio_{c}' for c in cat_spend_ratio.columns]
```

**Step 3 — Merge into customer_df:**
```python
customer_df = customer_df.join(cat_spend_ratio, on='Customer ID')
```

**Justification (write in markdown cell):** Category ratios reveal purchase *intent* — a customer spending 80% on Seasonal items is a holiday buyer, behaviorally distinct from a Home decor loyalist even if their RFM looks identical. This lifts cluster separation beyond pure spend volume.

**Sanity check:** `cat_spend_ratio.sum(axis=1).round(2).eq(1.0).all()` must be True (each customer's ratios sum to 1).

---

#### 3D — Outlier Handling

Document per feature using **both IQR and Z-score methods** — compare results, then justify which threshold you apply.

```python
# IQR method
Q1, Q3 = customer_df['Monetary'].quantile([0.25, 0.75])
IQR = Q3 - Q1
iqr_outliers = customer_df[(customer_df['Monetary'] < Q1 - 1.5*IQR) | 
                            (customer_df['Monetary'] > Q3 + 1.5*IQR)]

# Z-score method
from scipy import stats
z_scores = np.abs(stats.zscore(customer_df['Monetary']))
zscore_outliers = customer_df[z_scores > 3]

print(f"IQR outliers: {len(iqr_outliers)} | Z-score outliers: {len(zscore_outliers)}")
```

Apply to at minimum: `Monetary`, `Frequency`, `AvgBasketSize`.

| Feature | Typical skew | Recommended handling | Reason |
|---------|-------------|---------------------|--------|
| Monetary | Highly right-skewed | Cap at 99th percentile OR log-transform | Few VIP spenders pull mean far right |
| Frequency | Moderate right-skew | Cap at 99th percentile | Power buyers are real; don't delete |
| Recency | Less extreme | Check IQR; likely fine as-is | More uniform by nature |
| AvgBasketSize | Right-skewed | Cap at 99th percentile | Mirrors Monetary skew |

**Justify your choice (markdown cell):** State whether you capped or log-transformed Monetary and why. If you log-transform, apply `np.log1p()` (handles zero-spend edge case), and note that the feature is now on a log scale.

---

#### 3E — Scaling

**Decision required:** `StandardScaler` vs `RobustScaler` — explicitly compare and choose.

| Scaler | Formula | Best when |
|--------|---------|-----------|
| StandardScaler | `(x − μ) / σ` | Data is roughly normal after outlier handling |
| RobustScaler | `(x − median) / IQR` | Outliers remain in data; resistant to extreme values |

```python
from sklearn.preprocessing import StandardScaler, RobustScaler

# Try both; pick one and justify
scaler = StandardScaler()   # or RobustScaler()
X_scaled = scaler.fit_transform(customer_df[FEATURE_COLS])
X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURE_COLS, index=customer_df.index)

# Verify
print(X_scaled_df.mean().round(3))  # should be ≈ 0
print(X_scaled_df.std().round(3))   # should be ≈ 1 (StandardScaler) or robust equivalent
```

**Justification template (fill in your actual reasoning):**
> "I chose [Scaler] because after [capping/log-transforming] Monetary, the distribution is [approximately normal / still has residual outliers]. [StandardScaler] is appropriate here since distance-based algorithms (K-Means, DBSCAN) are sensitive to feature magnitude — without scaling, Monetary (~thousands) would dominate Recency (~days) purely due to scale difference, not information content."

**Sanity check:** `customer_df.shape[0] == df_clean['Customer ID'].nunique()` must be True before scaling.

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

**Step 1: Dendrogram — three linkage methods**

Sample 300 points: `np.random.choice(len(X_scaled), 300, replace=False)` — justify sample size (full 4000+ too slow for dendrogram rendering).

Run and plot dendrograms for **all three** linkage methods:

| Linkage | Method | Expected behaviour |
|---------|--------|-------------------|
| `ward` | Minimises within-cluster variance | Compact, evenly-sized clusters — usually best for RFM |
| `complete` | Max distance between clusters | Tighter clusters, sensitive to outliers |
| `single` | Min distance between clusters | Chaining effect — use to understand data topology, rarely deployed |

```python
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for ax, method in zip(axes, ['ward', 'complete', 'single']):
    Z = linkage(X_sample, method=method)
    dendrogram(Z, ax=ax, truncate_mode='lastp', p=20,
               show_contracted=True, no_labels=True)
    ax.set_title(f'Dendrogram — {method.capitalize()} Linkage')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Distance')
plt.tight_layout()
```

**Observation markdown cell:** For each linkage — where is the largest vertical gap? Does the suggested k agree across methods? Note that Single linkage likely shows chaining (one large cluster absorbing everything) — document this as an expected failure mode.

**Step 2: Fit AgglomerativeClustering**
```python
from sklearn.cluster import AgglomerativeClustering

for linkage_method, col in [('ward', 'Hierarchical_Ward'), 
                              ('complete', 'Hierarchical_Complete'),
                              ('single', 'Hierarchical_Single')]:
    model = AgglomerativeClustering(n_clusters=N_CLUSTERS_HIER, linkage=linkage_method)
    customer_df[col] = model.fit_predict(X_scaled)
```

- Compare cluster size distributions across all three columns
- Highlight if Single linkage collapsed into one dominant cluster (expected — document in Failure Log as S9 entry)

**Step 3: Profiles**
- `.groupby('Hierarchical_Ward')[['Recency', 'Frequency', 'Monetary']].mean()`
- Visualize with same axis style as K-Means for direct comparison

**Key questions to answer in markdown:**
- Did Ward and Complete produce similar groupings?
- Does Single linkage confirm the chaining problem?
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

**Compute for K-Means and Hierarchical Ward + Complete (all 3 metrics):**
- `silhouette_score(X_scaled, labels)`
- `davies_bouldin_score(X_scaled, labels)`
- `calinski_harabasz_score(X_scaled, labels)`

**Note on Hierarchical Single:** Silhouette only — Davies-Bouldin and Calinski-Harabasz are still valid but likely degenerate due to chaining. Compute them anyway and note the degenerate result.

**Compute for DBSCAN (Silhouette only, exclude noise):**
```python
mask = customer_df['DBSCAN_Cluster'] != -1
sil_dbscan = silhouette_score(X_scaled[mask], dbscan_labels[mask])
```
Explain in comment WHY noise excluded: noise points (-1) have no cluster membership; including them artificially biases the metric.

**Comparison table:**

| Method | N Clusters | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ |
|--------|-----------|-------------|-----------------|---------------------|
| K-Means | ? | ? | ? | ? |
| Hierarchical (Ward) | ? | ? | ? | ? |
| Hierarchical (Complete) | ? | ? | ? | ? |
| Hierarchical (Single) | ? | ? (degenerate) | ? | ? |
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
1. Try `StandardScaler` vs `RobustScaler` → observe whether residual outliers shift cluster centroids differently
2. Try k=2 vs k=8 — too few vs too many clusters and what happens to silhouette
3. DBSCAN with very small ε → everything becomes noise
4. Not removing cancelled orders → Monetary goes negative for some customers, clusters shift
5. Using raw Monetary (skewed) vs log-transformed Monetary → cluster shape difference
6. Single linkage hierarchical clustering → chaining effect causes one dominant cluster, illustrating why linkage choice matters

---

### Section 10 — High Ceiling (Optional)

Pick one if time allows:

| Option | What to do | Recommended for |
|--------|-----------|-----------------|
| A | K-Means from scratch (random + k-means++ init), compare vs sklearn | If you want to understand convergence |
| B | DBSCAN from scratch (`region_query`, `expand_cluster`), time complexity profile | If you want algorithmic depth |
| C | HDBSCAN with `hdbscan` library, compare vs DBSCAN | Easiest extension, strong comparison story |
| D | Apply pipeline to different domain dataset | If you have extra time |

**Recommendation:** Option C (HDBSCAN) — one import, one fit, strong comparison story, minimal extra code.

---

## Submission Checklist

- [ ] All cells executed top to bottom with no errors
- [ ] Every code block has comments explaining **WHY** (not just what)
- [ ] All plots have titles, axis labels, legends
- [ ] Observation markdown cells filled in (not left as `_Write here_`)
- [ ] Category spend ratios engineered (≥5 keyword categories, ratios verified to sum to 1)
- [ ] Outlier detection done with both IQR and Z-score; choice documented
- [ ] Scaler choice (StandardScaler vs RobustScaler) explicitly justified
- [ ] Cluster profiles computed for all 3 methods (K-Means, Hierarchical Ward, DBSCAN)
- [ ] Hierarchical clustering run for all three linkages: Ward, Complete, **Single**
- [ ] Comparison table built in Section 7 (including Single linkage row)
- [ ] Final model decision justified
- [ ] Business Narrative: one paragraph per cluster + 200–300 word executive summary
- [ ] Failure Log: minimum 3 entries, each with hypothesis / outcome / learning
- [ ] Single `.ipynb` file submitted (not a zip, not a `.py`)

---

## What Changed from v1 (Gap Summary)

| Gap | v1 Status | v2 Fix |
|-----|-----------|--------|
| Category spend ratios | Absent | Added as Section 3C with full keyword-bucketing implementation |
| Outlier detection | IQR only | Both IQR and Z-score now required; comparison documented |
| Scaler choice | StandardScaler hardcoded | Explicit StandardScaler vs RobustScaler decision with justification template |
| Single linkage | Not mentioned | Added to S5 with expected chaining failure documented; row added to S7 table |

---

## Time Estimate

| Section | Estimated Time |
|---------|---------------|
| S0–S1 (setup + load) | 20 min |
| S2 (cleaning) | 30 min |
| S3 (feature engineering incl. category ratios) | 90–120 min |
| S4 (K-Means) | 45 min |
| S5 (Hierarchical — 3 linkages) | 40 min |
| S6 (DBSCAN) | 45 min |
| S7 (validation) | 25 min |
| S8 (business narrative) | 45 min |
| S9 (failure log) | 20 min |
| **Total** | **~6.5–7 hours** |

**With 9 days to deadline (due 21 Jun), suggest: S0–S3 today, S4–S6 next session, S7–S9 final session.**

# fuseAiF_wk7_customer_segmentation

Market segmentation pipeline on UCI Online Retail II — RFM feature engineering, K-Means, Hierarchical, and DBSCAN clustering with business narrative and validation metrics.

---

## Context

**Fusemachines AI Fellowship 2026 | Week 7 | Phase 2: Foundational Statistical Learning**

A mid-sized retail company has ~500,000 raw transactions and no customer labels. The task is to construct a customer feature matrix from scratch, discover natural segments using three clustering algorithms, validate the results statistically, and translate findings into a business story a marketing team can act on.

---

## Dataset

[UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) — real-world transactional data from a UK-based online retailer, covering approximately 500,000 line items across two years. Sheet used: `Year 2010-2011`.

> The dataset is not included in this repository. Download the `.xlsx` file from the UCI link above and place it in the project root before running the notebook.

---

## Pipeline Overview

```
Raw transactions (500k rows)
        ↓
Data Cleaning
  - Drop null CustomerIDs
  - Remove cancellations (Invoice prefix 'C')
  - Drop Quantity ≤ 0 / Price ≤ 0
  - Parse InvoiceDate, create TotalPrice
        ↓
Feature Engineering → one row per customer
  - Recency, Frequency, Monetary (RFM)
  - AvgBasketSize, AvgDaysBetweenPurchases
  - UniqueProducts, ReturnRate
  - Category spend ratios (Gift / Home / Seasonal / Stationery / Other)
        ↓
Preprocessing
  - Outlier detection: IQR vs Z-score compared
  - Scaling: StandardScaler / RobustScaler (justified per data distribution)
        ↓
Clustering
  - K-Means       → Elbow + Silhouette for k; k-means++ vs random init comparison
  - Hierarchical  → Ward, Complete, Average, Single dendrograms; Ward + Complete fitted
  - DBSCAN        → k-distance ε estimation; ≥3 (ε, min_samples) combos; noise analysis
        ↓
Validation
  - Silhouette Score · Davies-Bouldin Index · Calinski-Harabasz Index
  - Cross-method comparison table
  - Final model decision: metrics + business reasoning
        ↓
Business Narrative
  - One-paragraph profile per cluster (plain language + RFM mean values)
  - Specific marketing action per segment
  - 200–300 word executive summary for non-technical stakeholders
```

---

## Repository Structure

```
fuseAiF_wk7_customer_segmentation/
├── Week_7_Clustering_Assignment.ipynb   # Main submission — all cells executed
├── README.md
└── online_retail_II.xlsx                # NOT included — download from UCI
```

---

## Key Techniques

| Stage | Method | Notes |
|-------|--------|-------|
| Feature engineering | RFM + 4 behavioral + 5 category ratios | Category ratios via keyword bucketing on `Description` |
| Outlier handling | IQR and Z-score | Both computed; choice justified per feature skew |
| Scaling | StandardScaler / RobustScaler | Selection depends on residual outlier presence post-capping |
| K-Means | `k-means++` init, k = 2–10 | Elbow + Silhouette used together; init stability compared |
| Hierarchical | Ward · Complete · Average · Single | All 4 dendrograms; Ward + Complete fitted to scaffold columns |
| DBSCAN | ε from k-distance plot | ≥3 param combos; noise points analyzed as business segment |
| Validation | Silhouette · Davies-Bouldin · Calinski-Harabasz | DBSCAN: noise excluded before metric computation |

---

## Results

*Populated after notebook completion.*

| Method | k | Silhouette ↑ | Davies-Bouldin ↓ | Calinski-Harabasz ↑ |
|--------|---|-------------|-----------------|---------------------|
| K-Means | — | — | — | — |
| Hierarchical (Ward) | — | — | — | — |
| DBSCAN | — | — | N/A | N/A |

**Final model:** *TBD*

---

## Cluster Segments

*Populated after notebook completion.*

| Cluster | Name | Key RFM Pattern | Recommended Action |
|---------|------|-----------------|-------------------|
| — | — | — | — |

---

## Setup

```bash
# Clone
git clone https://github.com/AaradhyaDT/fuseAiF_wk7_customer_segmentation.git
cd fuseAiF_wk7_customer_segmentation

# Install dependencies
pip install pandas numpy scikit-learn scipy seaborn matplotlib openpyxl

# Place dataset
# Download online_retail_II.xlsx from UCI and put it in the project root

# Run
jupyter notebook Week_7_Clustering_Assignment.ipynb
```

---

## Stack

Python · scikit-learn · scipy · Pandas · NumPy · Matplotlib · Seaborn

---

## Fellowship Context

This is Week 7 of the [Fusemachines AI Fellowship 2026](https://fusemachines.com), Phase 2: Foundational Statistical Learning. Previous weeks:

| Week | Project | Repo |
|------|---------|------|
| 3 | Text-to-SQL Agentic Pipeline | [fuseAiF_wk3_text2sql](https://github.com/AaradhyaDT/fuseAiF_wk3_text2sql) |
| 4 | Telco Churn & CLV ML Pipeline | [FUSE_AIF_2026_M1](https://github.com/AaradhyaDT/FUSE_AIF_2026_M1) |
| 5 | Telco Churn Tree-Based Ensembles | [fuseAiF_wk5_telco_churn_ensembles](https://github.com/AaradhyaDT/fuseAiF_wk5_telco_churn_ensembles) |

---

*Fusemachines AI Fellowship 2026 — Week 7 submission by Aaradhya Dev Tamrakar*

# 🛒 E-Commerce – Marketing Optimization

## 🏢 Client Brief: "Ukelele" – Global Online Retail Platform

### 📌 Company Overview
Ukelele is a fast-scaling e-commerce platform transitioning from a mid-sized retailer to a global leader. Operating across multiple countries and verticals, it seeks to embed data science across departments to break down silos and drive intelligent decision-making.

### 📉 Business Challenge
Despite increasing investments in marketing, conversions have plateaued and customer engagement is inconsistent. The leadership suspects that undifferentiated campaign strategies and poor customer targeting are leading to wasted spend and missed opportunities for growth.

### 🧩 Problem Statement
Ukelele’s marketing budget is expanding, but returns are not scaling proportionally. The team struggles with undifferentiated targeting, customer churn, and low cross-sell uptake. Leadership demands a sharper, data-driven understanding of customer behaviour to personalize marketing efforts.

---

## 📄 Project Brief: Sales & Customer Intelligence for Marketing

### 🧾 Project Title
**Driving Marketing Efficiency Through Behavioural Analytics & Predictive Customer Insights**

### 🎯 Objectives
Leverage historical transaction and marketing interaction data to:
- Identify distinct customer groups via RFM and clustering techniques  
- Predict high-value future customers for targeted retention and loyalty investments  
- Detect early churn signals and drive intervention strategies  
- Uncover frequent product pairings for bundling and personalized recommendations  
- Validate campaign effectiveness through controlled A/B testing  

---

## 📦 Dataset Summary

### 📚 Sources
- UCI Online Retail Dataset (for Segmentation, CLTV, Market Basket Analysis)  
- Kaggle: A/B Testing Dataset (for campaign performance evaluation)  

**Time Frame:**  
All timelines are aligned synthetically to simulate current operations

### 🗃️ Key Tables and Their Purpose

| Table         | Source             | Purpose                                                                 |
|---------------|--------------------|-------------------------------------------------------------------------|
| transactions  | UCI Online Retail  | Purchase history used for RFM analysis, CLTV prediction, and market basket modeling. |
| customers     | UCI Online Retail  | Basic customer profile with country, ID, and purchase activity.         |
| invoices      | UCI Online Retail  | Detailed line items for each transaction (Quantity, Unit Price, InvoiceNo, etc.). |
| user_data     | Kaggle Churn Dataset | Customer profiles with tenure, contract type, and churn status for classification modeling. |
| ab_test_results | Kaggle A/B Dataset | Conversion logs segmented by control/test group, used for uplift and campaign evaluation. |

### 🔑 Key Variables Across Datasets

**From UCI Online Retail:**
- `CustomerID`, `InvoiceDate`, `InvoiceNo`, `Country` → used for cohort and RFM features  
- `Quantity`, `UnitPrice` → used to compute revenue, CLTV, and basket patterns  
- `Description` → product-level text used in market basket analysis  
- `InvoiceNo` with negative `Quantity` → used to infer returns  

**From A/B Test Dataset:**
- `user_id`, `group` (control/test), `converted`, `timestamp` → used to calculate conversion rate, uplift, and statistical significance  
- Region and device info if available can be used for segment-level testing  

---

## 📊 Key Business Metrics

| Metric                        | Why It Matters                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| CLTV (Customer Lifetime Value) | Optimizes acquisition spend, loyalty programs, and retention targeting.        |
| Churn Rate                   | Guides retention strategies by identifying at-risk customers.                  |
| Conversion Rate              | Measures effectiveness of campaigns, landing pages, and marketing messaging.   |
| Basket Lift (Lift Index)     | Improves cross-sell and bundling strategies.                                   |
| Segment ROI                  | Informs budget allocation across segments.                                     |
| A/B Test Uplift              | Quantifies campaign performance improvements.                                  |
| Email Click-Through Rate     | Tracks engagement with personalized campaigns.                                 |
| Repeat Purchase Rate         | Indicates loyalty and retention success.                                       |
| Time Between Purchases       | Determines lifecycle stages and timing for re-engagement.                      |
| Return Rate by Segment       | Highlights segment-specific profitability issues.                              |
| Channel CLTV                 | Measures long-term value of customers from each acquisition channel.           |
| Campaign Attribution ROI     | Assesses ROI of individual marketing efforts.                                  |

---

## 📦 Key Deliverables

### 📊 Analytical Reports
- `01_rfm_segmentation.ipynb`  
- `02_cltv_prediction.ipynb`  
- `03_churn_prediction.ipynb`  
- `04_market_basket_analysis.ipynb`  
- `05_ab_test_campaigns.ipynb`  

### 📑 Business-Insights Reports
- Segment profiles and ROI  
- Churn heatmaps and trends  
- Top cross-sell associations  
- Campaign variant test results  

### 📌 Actionable Recommendations
- Which customers to target for upsell, retention  
- When to send campaigns for maximum engagement  
- What product bundles convert best  

---

## 💥 Expected Business Impact

- 📈 **+15% conversion rate** via targeted segmentation  
- 📉 **-10% churn** from timely retention outreach  
- 💰 **₹3,00,000 savings** via reduced campaign waste  

---

## 🧩 Project Structure

> *(Add your file/folder structure here if needed, e.g. project/src, data/, notebooks/, etc.)*

---

## 🛠 Tools & Libraries
- Python (`pandas`, `sklearn`, `mlxtend`)  
- Plotly, seaborn  
- Jupyter  
- Excel (for lift simulation)  

---

## 🧠 Assumptions

### 🧩 Business-Level Assumptions

| Area                   | Assumption                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Customer Behavior      | Each customer ID maps to a unique user with consistent behavior.           |
| Churn Definition       | Customer is "churned" if inactive for 6+ months (UCI) or labeled churn (Kaggle). |
| CLTV Time Horizon      | Estimated using 6 months of past behavior.                                 |
| Marketing Strategy     | A/B tests simulate seasonal/product-based campaigns.                       |
| Email Engagement       | CTR assumed or simulated.                                                  |
| Geography              | Country used for region-level segmentation.                                |

### 🔍 Data-Level Assumptions

| Area                   | Assumption                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Revenue Calculation    | Revenue = `Quantity × UnitPrice`; negative quantities are returns.         |
| Product Co-occurrence  | Market Basket based on `InvoiceNo` representing sessions.                  |
| Data Quality           | Cleaned data: no duplicates, standardized formats.                         |
| Campaign Assignment    | A/B test groups are random and balanced.                                   |
| Channel Attribution    | Simulated if not present.                                                  |

### 📈 Modeling Assumptions

| Area                   | Assumption                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Segmentation Inputs    | RFM features use a consistent reference date.                              |
| CLTV Modeling          | Probabilistic or regression-based modeling.                                |
| Churn Modeling         | Uses structured profile and behavioral features.                           |
| A/B Testing Validity   | Experiment run time ensures statistical significance.                      |

---

## 📌 Next Steps
1. Finalize preprocessing pipeline for merged datasets  
2. Validate assumptions through exploratory data analysis  
3. Build initial segmentation and CLTV models  
4. Schedule stakeholder review for marketing strategy alignment  


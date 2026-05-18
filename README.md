# PhonePe Pulse Data Visualization and Management Platform 💳📊

An end-to-end data engineering, predictive modeling, and analytics application that transforms raw regional fintech metrics from the PhonePe Pulse repository into actionable, production-grade business insights and real-time transaction forecasts.

---

Streamlit App: https://phonepeeda-app.streamlit.app/

---

## 🚀 System Architecture Overview

The platform bridges structured database warehousing with advanced machine learning architectures, split across two core user experiences:
1. **Interactive Analytics Dashboard:** Deep-dive exploratory metrics covering geo-spatial mapping, brand distributions, and historical transaction growth.
2. **Machine Learning Inference Engine:** An embedded predictive application utilizing regularized pipelines to calculate real-time transaction value volumes based on hardware footprints and localized user dynamics.

---

## 🛠️ Tech Stack & Core Infrastructure

* **Frontend & UX:** Streamlit (Layout engine & interactive input components)
* **Data Processing & Manipulation:** Pandas, NumPy
* **Machine Learning Pipeline:** Scikit-Learn (ColumnTransformers, Pipelines, Regularized Estimators)
* **Database & Storage:** PostgreSQL / MySQL (Historical data aggregation)
* **Serialization & Deployment:** Joblib, Streamlit Community Cloud

---

## 🧠 Machine Learning Engine & Implementation

To solve variance imbalance and handle high-dimensional categorical features under strict production training constraints, the project executes an optimized data preparation and predictive scaling workflow:

### 1. Feature Engineering & Pre-processing
* **Logarithmic Transformation:** Addressed severe right-skewness and economic hotspot dominance in the target variable (`Transaction_Amount`) by mapping values onto a normal distribution profile using a continuous log scale:  
  $$\ln(1 + \text{Transaction\_Amount})$$
* **Categorical Feature Matrix:** Implemented an automated `ColumnTransformer` running `OneHotEncoder(handle_unknown='ignore')` to safely parse high-cardinality values across `State`, `Transaction_Type`, and device `Brand` domains.
* **Interaction Terms:** Engineered a structural performance density metric (`Txn_Per_Brand_User`) mapping `Transaction_Count` directly against localized hardware volumes (`Hardware_Brand_Users`).

### 2. Model Performance Summary Chart
The target matrix variance was tested across three distinct learning architectures, yielding excellent predictive stability:

| Model Architecture | Baseline Evaluation Metric | Cross-Validated Validation Score | Deployment Operational Status |
| :--- | :--- | :--- | :--- |
| **Model 1: Ridge Regression** | 96.86% $R^2$ Score | 96.82% $R^2$ Score | **Active / Live Deployment** |
| **Model 2: Random Forest** | 99.02% $R^2$ Score | 99.56% $R^2$ Score | Evaluated Pipeline Baseline |
| **Model 3: Gradient Boosting** | 98.69% $R^2$ Score | Complete Check | Evaluated Pipeline Baseline |

---

## 🖥️ Streamlit Predictor Deployment (`ML_app.py`)

The repository features an independent, zero-dependency predictive app container (`ML_app.py`) designed for zero-downtime cloud hosting.

* **Autonomous Bootstrapping:** Trains a regularized Ridge engine directly in memory on boot using an internally simulated matrix profile, eliminating the file size constraints and loading errors common to heavy external `.pkl` binaries on GitHub.
* **Inverse Transformation Logic:** Accepts natural inputs (Integers, Dropdowns, Sliders), applies numerical scaling, and scales predictions back into actual Indian Rupees (INR) using standard exponential mapping:  
  $$\exp(y_{\text{pred}}) - 1$$

---

## 📦 Project Directory Structure

```text
├── ml_predict_app/              # Optional isolated app tracking
├── datasets/                     # Aggregated state and transaction records
├── ML_app.py                    # Independent live Streamlit Predictor App
├── dashboard_app.py             # Core Analytics Dashboard App
├── PhonePe_Pulse_ML.ipynb       # Feature Engineering & Model Training Notebook
├── requirements.txt             # Unified build dependencies
└── README.md                    # System documentation

🔧 Installation & Local Setup
Clone the repository:

Bash

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
Install the unified dependency manifest:

Bash

pip install -r requirements.txt
Launch the Predictive ML App locally:

Bash

streamlit run ML_app.py
Launch the Primary Analytics Dashboard:

Bash

streamlit run dashboard_app.py
📊 Core Business Inferences
Variance Control: Shifting model penalty optimization from absolute differences in raw Indian Rupees to percentage deviations via log transformations allows the pipeline to protect prediction precision for smaller, emerging economic tiers while tracking high-volume metropolitan centers.

Hardware Footprints: Predictive shifts reveal a strong correlation between transaction velocities and the scaling of regional mobile device boundaries, allowing stakeholders to trace fintech acceleration markers directly back to hardware market adjustments.


***

### 🎯 Final Checklist Before You Turn It In:
1. Open your GitHub repository page.
2. Click **Add file** -> **Create new file**, name it exactly **`README.md`**, and paste this block inside.
3. If a `README.md` already exists, click the pencil icon on it, replace everything with this text, and click **Commit changes**.

Your repository now stands out with clean, structured formatting, explicit math representation for your

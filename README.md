# PhonePe Pulse Data Visualization & Exploration Platform

> An automated data engineering and interactive analytics platform that transforms semi-structured transactional and user data from the PhonePe Pulse repository into actionable, regional market insights.

---

## 🚀 Project Overview

This project is an end-to-end data product designed to solve the **"Cold Start" data challenge** by transforming an intimidating expanse of unstructured raw records into an intuitive, predictive asset for market expansion.

The system operates in two core environments:

1. 
**The Backend Engineering Pipeline (Google Colab):** Automatically traverses, extracts, sanitizes, and maps complex multi-tiered JSON file systems into highly optimized relational sheets.


2. **The Analytics Interface (Streamlit Application):** Consumes the structured data layer to serve dynamic vertical scrolling canvas cards, utilizing high-contrast visual hierarchies to surface micro-retail habits, hardware dominance, and geographic adoption patterns.

---

Dataset Repo Link: https://github.com/PhonePe/pulse 

---

## 🏗️ Technical Architecture

### 1. The 8-Pillar Data Pipeline (Google Colab Backend)

The ingestion infrastructure systematically flattens and structures massive, nested directory trees ordered by calendar years, quarters, and regional states.

* **Environment Initialization:** Binds operating system path utilities (`os`) and initializes vector memory engines (`Pandas`) to manage massive metadata object trees in memory safely.


* **Traversals & Matrix Splitting:** Utilizes an aggressive `os.walk` path engine to drill into deep folder nests and isolate metrics across three highly discrete vectors: **Aggregated**, **Map**, and **Top** characteristics.


* **Nested Flattening & Serialization:** Extracts hidden dictionary attributes from raw JSON objects, compiling the flattened linear results into **nine distinct relational tables** exported as optimized CSV sheets (the unified Single Source of Truth).


* **Sanitation Layer:** Eliminates statistical distortion and duplication by actively purging generic national entries (such as those under the explicit state designation `"India"`) while enforcing strict datatype coercion to ensure pristine computational floats and integers.



### 2. Interactive Visualization Canvas (Streamlit Frontend)

The frontend layer bypasses cramped, multi-column grid dashboards in favor of a clean, vertical, card-based scroll hierarchy to promote layout hygiene and quick cognitive scanning.

* **Plotly Express Engine:** Built-in interactive charts incorporate a custom continuous color scale transitioning smoothly from **Soft Light Lavender** to **Midnight Purple** to ensure lower-volume regional elements maintain clear visual presence against the background.
* **Geographic GeoJSON Mapping:** Plots geometric distribution patterns across states and districts, instantly turning complex data points into intuitive spatial stories.

---

## 📈 Strategic Business Insights Covered

The application analyzes real-world case studies to drive operational strategies:

* **Core Payments Analysis:** Surfaces a profound behavioral transition where early platform volume was dominated by peer-to-peer (P2P) transfers, but everyday micro-retail shopping habits are now compounding at a far superior velocity via Merchant Payments.


* **Hardware Ecosystem Mapping:** Exposes a stark market oligopoly where Android budget device manufacturers (specifically Xiaomi, Samsung, and Vivo) command the absolute majority of the national subscriber base. This informs product engineers to aggressively prioritize memory optimization to minimize application churn.
* **Cyclical Protection Ingestion:** Uncovers right-skewed metric distributions for digital insurance policies, revealing that adoption is currently concentrated within affluent technology hubs like Bengaluru Urban and Pune. Longitudinal evaluation reveals predictable, systemic spikes during the fourth and first quarters of consecutive fiscal years, directly correlating consumer adoption with financial year-end tax planning.

---

## 🎯 Targeted Prescriptions

Based on these hot-spot and empirical trends, the platform yields three actionable enterprise directives:

1. Deploy targeted offline merchant acquisition and cost-effective **Soundbox hardware subscriptions** within rising Tier-2 and Tier-3 urban ecosystems to capture daily high-frequency retail loops.


2. Concentrate high-velocity marketing expenditure directly inside the epicenter pin codes identified by the hotspot analysis to pilot premium **wealth management architectures**.


3. Move away from generic, passive layouts for secondary financial instruments; instead, deploy **contextual, transaction-triggered notifications** (e.g., prompting a micro-insurance policy immediately following a successful automotive merchant payment) to capitalize on cyclical intent windows.

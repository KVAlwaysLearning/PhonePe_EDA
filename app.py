import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")

# --- DATA LOADING (Example) ---
# Ensure your CSVs are in the 'PhonePe_CSV_Data' folder we created
@st.cache_data
def load_data():
    # Load your main tables for visualization
    agg_trans = pd.read_csv('PhonePe_CSV_Data/aggregated_transaction.csv')
    agg_user = pd.read_csv('PhonePe_CSV_Data/aggregated_user.csv')
    agg_ins = pd.read_csv('PhonePe_CSV_Data/aggregated_insurance.csv')
    return agg_trans, agg_user, agg_ins

try:
    df_trans, df_user, df_ins = load_data()
except Exception as e:
    st.error(f"Please ensure CSV files are present: {e}")
    st.stop()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Section", 
    ["Project Overview", "Transaction Analysis", "User Engagement", "Insurance Insights"])

# --- GLOBAL FILTERS ---
st.sidebar.markdown("---")
st.sidebar.header("Global Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(df_trans['Year'].unique(), reverse=True))
selected_state = st.sidebar.selectbox("Select State", sorted(df_trans['State'].unique()))

# --- PAGE: PROJECT OVERVIEW ---
if page == "Project Overview":
    st.title("PhonePe Transaction Insights (2018-2024)")
    st.markdown("""
    This project analyzes digital payment dynamics, user engagement, and insurance trends 
    to provide actionable business recommendations.
    """)
    
    # High-level Metrics (KPIs)
    col1, col2, col3 = st.columns(3)
    total_vol = df_trans[df_trans['Year'] == selected_year]['Count'].sum()
    total_rev = df_trans[df_trans['Year'] == selected_year]['Amount'].sum()
    
    col1.metric("Total Transactions", f"{total_vol:,}")
    col2.metric("Total Revenue (INR)", f"₹{total_rev:,.2f}")
    col3.metric("Selected State", selected_state)

# --- PAGE: TRANSACTION ANALYSIS (Where your charts go) ---
elif page == "Transaction Analysis":
    st.header(f"Transaction Insights for {selected_state} ({selected_year})")
    
    # Filtered Data for charts
    filtered_df = df_trans[(df_trans['State'] == selected_state) & (df_trans['Year'] == selected_year)]
    
    # --- INSERT CHART 1.1 (Modified for Streamlit) ---
    st.subheader("Transaction Volume by Type")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=filtered_df, x='Type', y='Count', palette='Blues_d', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # --- INSERT CHART 1.2 (Pie Chart) ---
    st.subheader("Transaction Mix")
    fig2, ax2 = plt.subplots()
    type_mix = filtered_df.groupby('Type')['Count'].sum()
    ax2.pie(type_mix, labels=type_mix.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(fig2)

# --- (Other pages follow a similar pattern) ---

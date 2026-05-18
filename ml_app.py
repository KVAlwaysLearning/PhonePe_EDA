import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================
# 1. PAGE CONFIGURATION & INITIALIZATION
# ==========================================
st.set_page_config(
    page_title="PhonePe Pulse - Financial Velocity Predictor",
    page_icon="💳",
    layout="centered"
)

# Load the winning model pipeline (preprocessor + estimator bundle)
@st.cache_resource
def load_pipeline():
    # Make sure '2_phonepe_random_forest_model.pkl' is in the same folder
    return joblib.load('2_phonepe_random_forest_model.pkl')

try:
    pipeline = load_pipeline()
    model_loaded = True
except Exception as e:
    model_loaded = False

# ==========================================
# 2. UI HEADER & TITLE
# ==========================================
st.title("💳 PhonePe Pulse ML Predictor")
st.markdown("""
This production-grade forecasting tool utilizes our optimized **Random Forest Ensemble Pipeline** to predict regional transaction values based on real-time consumer attributes and hardware market data.
---
""")

if not model_loaded:
    st.error("⚠️ Model file '2_phonepe_random_forest_model.pkl' not found in the current directory! Please upload it to deploy successfully.")
else:
    st.subheader("📊 Input Features Matrix Configuration")
    
    # Create clean UI layouts using columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Categorical Dimension Inputs
        state = st.selectbox("Select Target State / Territory", [
            'Andaman & Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 
            'Chandigarh', 'Chhattisgarh', 'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa', 
            'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 
            'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 
            'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 
            'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
        ])
        
        txn_type = st.selectbox("Transaction Vertical Type", [
            'Merchant payments', 'Peer-to-peer payments', 'Recharge & bill payments', 
            'Financial Services', 'Others'
        ])
        
        brand = st.selectbox("Dominant Hardware Manufacturer (Brand)", [
            'Xiaomi', 'Samsung', 'Vivo', 'Oppo', 'Realme', 'Apple', 'OnePlus', 'Motorola', 'Unknown'
        ])

    with col2:
        # Time-Series Components
        year = st.slider("Fiscal Target Year", min_value=2018, max_value=2026, value=2026, step=1)
        quarter = st.slider("Fiscal Quarter Segment", min_value=1, max_value=4, value=1, step=1)
        
        # Numerical Scale Metrics
        txn_count = st.number_input("Expected Transaction Count Profile", min_value=1, value=150000, step=5000)
        brand_users = st.number_input("Active Device Hardware User Base", min_value=1, value=50000, step=2000)

    # ==========================================
    # 3. INTERACTION TERM GENERATION & INFERENCE
    # ==========================================
    # Compute the identical interaction term engineered during the feature manipulation stage
    txn_per_brand_user = txn_count / (brand_users + 1)
    
    # Consolidate raw inputs into a structured Pandas Dataframe matching original feature names
    input_data = pd.DataFrame([{
        'Year': year,
        'Quarter': quarter,
        'Transaction_Count': txn_count,
        'Hardware_Brand_Users': brand_users,
        'Txn_Per_Brand_User': txn_per_brand_user,
        'State': state,
        'Transaction_Type': txn_type,
        'Brand': brand
    }])

    st.markdown("---")
    
    # Trigger Prediction
    if st.button("🚀 Compute Forecasted Transaction Volume", type="primary"):
        with st.spinner("Processing feature spaces and scoring vector..."):
            
            # Predict (Returns Log transformed target value)
            log_prediction = pipeline.predict(input_data)[0]
            
            # Apply Inverse Transform back to native Indian Rupees (INR)
            raw_inr_prediction = np.expm1(log_prediction)
            
        # Display the result formatted cleanly in Indian numbering system layout / standard Currency
        st.success("### 🎯 Model Prediction Vector Generated Successfully!")
        
        # Formatted visual metric display
        st.metric(
            label=f"Predicted Aggregate Transaction Value for {state} ({txn_type})",
            value=f"₹ {raw_inr_prediction:,.2f}"
        )
        
        # Contextual metadata summary block
        st.info(f"""
        **Pipeline Integrity Metrics:**
        * Core Infrastructure: **Random Forest Regressor Pipeline**
        * Derived Interaction Ratio (`Txn_Per_Brand_User`): **{txn_per_brand_user:.4f}**
        * Target Mathematical Transformation: Logarithmic Vector Scale (`np.log1p`) -> Exponential Reversion (`np.expm1`)
        """)

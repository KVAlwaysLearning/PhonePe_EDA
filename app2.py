import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PhonePe Pulse Comprehensive Analytics Dashboard", 
    layout="wide", 
    page_icon="🔮"
)

# --- PHONEPE STYLING & DESIGN UPGRADE ---
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); border: 1px solid #e1e4e8; }
    h1, h2, h3 { color: #5d2e8e; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .chart-container { background-color: #ffffff; padding: 25px; border-radius: 12px; margin-bottom: 25px; border: 1px solid #e6ebf1; box-shadow: 0 2px 4px rgba(0,0,0,0.01); }
    </style>
    """, unsafe_allow_html=True)

# --- OPTIMIZED CACHED DATA INGESTION ENGINE ---
@st.cache_data
def load_all_pulse_tables():
    tables = [
        'aggregated_transaction', 'aggregated_user', 'aggregated_insurance',
        'map_transaction', 'map_user', 'map_insurance',
        'top_transaction', 'top_user', 'top_insurance'
    ]
    data_store = {}
    for table in tables:
        try:
            data_store[table] = pd.read_csv(f'PhonePe_CSV_Data/{table}.csv')
        except Exception as e:
            st.error(f"❌ Critical Error: Unable to read file 'PhonePe_CSV_Data/{table}.csv'. Reason: {e}")
            st.stop()
    return data_store

dfs = load_all_pulse_tables()

# --- GLOBAL FILTER SIDEBAR CONTROL ---
st.sidebar.image("https://www.phonepe.com/badges/PhonePe_Logo.png", width=160)
st.sidebar.markdown("### National Context Filtering")

available_years = ["ALL"] + sorted(dfs['aggregated_transaction']['Year'].unique().astype(str).tolist(), reverse=True)
available_states = ["ALL"] + sorted(dfs['aggregated_transaction']['State'].unique().tolist())

selected_year = st.sidebar.selectbox("Global Year Filter", available_years)
selected_state = st.sidebar.selectbox("Global State/UT Filter", available_states)

st.sidebar.markdown("---")
domain_selector = st.sidebar.radio(
    "Select Analysis Core Domain",
    [
        "Case 1: Core Payments",
        "Case 2: Hardware Ecosystem",
        "Case 3: Base Insurance",
        "Case 4: Market Expansion",
        "Case 5: Platform Engagement",
        "Case 6: Insurance Ingestion",
        "Case 7: Geographic Hotspots",
        "Case 8: User Onboarding",
        "Case 9: Strategic Protection"
    ]
)

# --- OPTIMIZED DATA FILTERING ROUTINE ---
def slice_dataframe(dataframe, year_col='Year', state_col='State', target_q="ALL"):
    working_df = dataframe.copy()
    
    # 1. Handle Year Filter
    if selected_year != "ALL" and year_col in working_df.columns:
        working_df = working_df[working_df[year_col] == int(selected_year)]
        
    # 2. Handle State Filter (The Fix)
    if state_col in working_df.columns:
        if selected_state != "ALL":
            # If a specific state is chosen, filter down to just that state
            working_df = working_df[working_df[state_col] == selected_state]
        else:
            # If "ALL" states are chosen, exclude the pre-aggregated 'India' rows 
            # so individual states don't get squished by the massive national total
            working_df = working_df[working_df[state_col] != "India"]
            
    # 3. Handle Quarter Filter
    if target_q != "ALL" and 'Quarter' in working_df.columns:
        working_df = working_df[working_df['Quarter'] == int(target_q)]
        
    return working_df

# --- HEADER FRAME ---
st.title("🔮 PhonePe Pulse Ecosystem Master Dashboard")
st.write(f"🔬 Currently Evaluating: **{domain_selector}** | **Scope State:** `{selected_state}` | **Scope Year:** `{selected_year}`")
st.markdown("---")

# --- CONCURRENT TABS GENERATION ---
quarter_tabs = st.tabs(["Combined Temporal Data", "Quarter 1 (Jan-Mar)", "Quarter 2 (Apr-Jun)", "Quarter 3 (Jul-Sep)", "Quarter 4 (Oct-Dec)"])

for q_idx, active_tab in enumerate(quarter_tabs):
    with active_tab:
        current_quarter = "ALL" if q_idx == 0 else str(q_idx)
        
        # ==========================================
        # CASE STUDY 1: CORE PAYMENTS
        # ==========================================
        if domain_selector == "Case 1: Core Payments":
            sub_df = slice_dataframe(dfs['aggregated_transaction'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("No dynamic payload matches these dimensional parameters.")
            else:
                with st.container():
                    st.markdown(f"""<div class="chart-container">
                    <h3 style="margin-bottom: 5px;">1.1 Univariate: Transaction Frequency</h3>
                    </div>""",unsafe_allow_html=True)
                    #st.markdown("### 1.1 Univariate: Transaction Frequency")
                    #v_data = sub_df.groupby('State')['Count'].sum().sort_values(ascending=False).reset_index()
                    #fig = px.bar(v_data, x='State', y='Count', color='Count', color_continuous_scale='purples', height=500)
                    #st.plotly_chart(fig, use_container_width=True)
                    #st.markdown('</div>', unsafe_allow_html=True)

                    # 2. Process your Plotly visualization logic data split
                    v_data = sub_df.groupby('State')['Count'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(v_data, x='State', y='Count', color='Count', color_continuous_scale='purples', height=500)
    
                    # 3. Render the interactive graph canvas directly inside the working window layout
                    st.plotly_chart(fig, use_container_width=True)    

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 1.2 Bivariate: Mix by Payment Type")
                    m_data = sub_df.groupby('Type')['Count'].sum().reset_index()
                    fig = px.pie(m_data, values='Count', names='Type', hole=0.3, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 1.3 Multivariate: Value Trends Over Time")
                    t_data = sub_df.groupby(['Year', 'Type'])['Amount'].sum().reset_index()
                    fig = px.line(t_data, x='Year', y='Amount', color='Type', markers=True, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 2: HARDWARE ECOSYSTEM
        # ==========================================
        elif domain_selector == "Case 2: Hardware Ecosystem":
            sub_df = slice_dataframe(dfs['aggregated_user'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("No data found for the current filter configuration.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 2.1 Univariate: Brand User Distribution")
                    b_dist = sub_df.groupby('Brand')['Count'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(b_dist, x='Brand', y='Count', color='Brand', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 2.2 Bivariate: Brand Market Share Stability")
                    s_data = sub_df.groupby(['Year', 'Brand'])['Percentage'].mean().reset_index()
                    fig = px.line(s_data, x='Year', y='Percentage', color='Brand', markers=True, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 2.3 Multivariate: Segmented Yearly Growth")
                    g_data = sub_df.groupby(['Year', 'Brand'])['Count'].sum().reset_index()
                    fig = px.bar(g_data, x='Year', y='Count', color='Brand', barmode='stack', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 3: BASE INSURANCE
        # ==========================================
        elif domain_selector == "Case 3: Base Insurance":
            sub_df = slice_dataframe(dfs['aggregated_insurance'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("No data found matching specifications.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 3.1 Univariate: Policy Count Density")
                    fig = px.histogram(sub_df, x='Count', marginal='rug', color_discrete_sequence=['#ff7f0e'], height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 3.2 Bivariate: Cumulative Adoption by State")
                    st_pols = sub_df.groupby('State')['Count'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(st_pols, x='State', y='Count', color='Count', color_continuous_scale='plasma', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 3.3 Multivariate: Top 10 Premium Trends")
                    top10_st = sub_df.groupby('State')['Amount'].sum().nlargest(10).index
                    f_df = sub_df[sub_df['State'].isin(top10_st)].groupby(['Year', 'State'])['Amount'].sum().reset_index()
                    fig = px.bar(f_df, x='Year', y='Amount', color='State', barmode='group', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 4: MARKET EXPANSION
        # ==========================================
        elif domain_selector == "Case 4: Market Expansion":
            sub_df = slice_dataframe(dfs['map_transaction'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("Zero row structures match the active matrix.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 4.1 Univariate: Market Size by State")
                    st_rev = sub_df.groupby('State')['Amount'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(st_rev, x='State', y='Amount', color='Amount', color_continuous_scale='viridis', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 4.2 Bivariate: National Scale Timeline")
                    yr_rev = sub_df.groupby('Year')['Amount'].sum().reset_index()
                    fig = px.line(yr_rev, x='Year', y='Amount', markers=True, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 4.3 Multivariate: Revenue Trajectory Top 5")
                    top5_rev = sub_df.groupby('State')['Amount'].sum().nlargest(5).index
                    f_df = sub_df[sub_df['State'].isin(top5_rev)].groupby(['Year', 'State'])['Amount'].sum().reset_index()
                    fig = px.line(f_df, x='Year', y='Amount', color='State', markers=True, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 5: PLATFORM ENGAGEMENT
        # ==========================================
        elif domain_selector == "Case 5: Platform Engagement":
            sub_df = slice_dataframe(dfs['map_user'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("Empty matrix slice caught.")
            else:
                # Dynamic column mapping to support both 'Count' or 'AppOpens' / 'RegisteredUsers' configurations
                eng_col = 'AppOpens' if 'AppOpens' in sub_df.columns else ('Count' if 'Count' in sub_df.columns else None)
                user_col = 'RegisteredUsers' if 'RegisteredUsers' in sub_df.columns else ('Users' if 'Users' in sub_df.columns else None)
                
                if not eng_col:
                    st.error("Could not find an engagement column (Count or AppOpens) in map_user dataset.")
                else:
                    with st.container():
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.markdown("### 5.1 Univariate: Engagement Profile")
                        st_eng = sub_df.groupby('State')[eng_col].sum().sort_values(ascending=False).reset_index()
                        fig = px.bar(st_eng, x='State', y=eng_col, color=eng_col, color_continuous_scale='oranges', height=500)
                        st.plotly_chart(fig, use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    with st.container():
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.markdown("### 5.2 Bivariate: Regional Distribution Over Time")
                        yr_eng = sub_df.groupby('Year')[eng_col].sum().reset_index()
                        fig = px.bar(yr_eng, x='Year', y=eng_col, height=500)
                        st.plotly_chart(fig, use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    with st.container():
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.markdown("### 5.3 Multivariate: Spatiotemporal Intensity")
                        h_map = sub_df.groupby(['State', 'Year'])[eng_col].mean().reset_index()
                        fig = px.density_heatmap(h_map, x='Year', y='State', z=eng_col, color_continuous_scale='blues', height=500)
                        st.plotly_chart(fig, use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
        # ==========================================
        # CASE STUDY 6: INSURANCE INGESTION
        # ==========================================
        elif domain_selector == "Case 6: Insurance Ingestion":
            sub_df = slice_dataframe(dfs['map_insurance'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("No row data maps to filters.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 6.1 Univariate: Penetration Scaler")
                    ins_scale = sub_df.groupby('State')['Count'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(ins_scale, x='State', y='Count', color='Count', color_continuous_scale='magma', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 6.2 Bivariate: Elite Top 15 Analysis")
                    top15_ins = sub_df.groupby('State')['Count'].sum().nlargest(15).reset_index()
                    fig = px.bar(top15_ins, x='State', y='Count', color_discrete_sequence=['#471354'], height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 6.3 Multivariate: Top 5 Quarterly Flow")
                    top5_ins = sub_df.groupby('State')['Count'].sum().nlargest(5).index
                    f_df = sub_df[sub_df['State'].isin(top5_ins)].groupby(['Quarter', 'State'])['Count'].sum().reset_index()
                    fig = px.bar(f_df, x='Quarter', y='Count', color='State', barmode='group', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 7: GEOGRAPHIC HOTSPOTS
        # ==========================================
        elif domain_selector == "Case 7: Geographic Hotspots":
            sub_df = slice_dataframe(dfs['top_transaction'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("No regional records parsed.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 7.1 Univariate: Macro Value Hotspots")
                    st_perf = sub_df.groupby('State')['Amount'].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(st_perf, x='State', y='Amount', color='Amount', color_continuous_scale='viridis', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 7.2 Bivariate: Volume vs Value Velocity")
                    fig = px.scatter(sub_df, x='Count', y='Amount', opacity=0.4, color_discrete_sequence=['green'], height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 7.3 Multivariate: Annual Top 10 Retention")
                    top10_st = sub_df.groupby('State')['Amount'].sum().nlargest(10).index
                    f_df = sub_df[sub_df['State'].isin(top10_st)].groupby(['State', 'Year'])['Amount'].sum().reset_index()
                    fig = px.bar(f_df, x='State', y='Amount', color='Year', barmode='group', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 8: USER ONBOARDING
        # ==========================================
        elif domain_selector == "Case 8: User Onboarding":
            sub_df = slice_dataframe(dfs['top_user'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("Onboarding profiles data row empty.")
            else:
                # Dynamic column mapping to detect your exact user count label
                user_count_col = 'Count' if 'Count' in sub_df.columns else ('RegisteredUsers' if 'RegisteredUsers' in sub_df.columns else sub_df.columns[-1])
                
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 8.1 Univariate: Registration Density")
                    fig = px.histogram(sub_df, x=user_count_col, nbins=20, color_discrete_sequence=['orange'], height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 8.2 Bivariate: Growth Velocities")
                    reg_y = sub_df.groupby('Year')[user_count_col].sum().reset_index()
                    fig = px.bar(reg_y, x='Year', y=user_count_col, color_discrete_sequence=['#2ca02c'], height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 8.3 Multivariate: Cohort Cyclicity")
                    reg_yq = sub_df.groupby(['Year', 'Quarter'])[user_count_col].sum().reset_index()
                    reg_yq['Quarter'] = reg_yq['Quarter'].astype(str)
                    fig = px.line(reg_yq, x='Year', y=user_count_col, color='Quarter', markers=True, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # ==========================================
        # CASE STUDY 9: STRATEGIC PROTECTION
        # ==========================================
        elif domain_selector == "Case 9: Strategic Protection":
            sub_df = slice_dataframe(dfs['top_insurance'], target_q=current_quarter)
            
            if sub_df.empty:
                st.warning("Strategic security trace is null for current setup.")
            else:
                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 9.1 Univariate: Hotspot Density Profile")
                    fig = px.histogram(sub_df, x='Count', marginal='violin', nbins=20, height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 9.2 Bivariate: Volume Leaders (Top 15)")
                    top15_st = sub_df.groupby('State')['Count'].sum().sort_values(ascending=False).head(15).reset_index()
                    fig = px.bar(top15_st, x='State', y='Count', color='Count', color_continuous_scale='electric', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with st.container():
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("### 9.3 Multivariate: Quarterly Box Spreads")
                    top5_st = sub_df.groupby('State')['Count'].sum().nlargest(5).index
                    f_df = sub_df[sub_df['State'].isin(top5_st)]
                    f_df['Quarter'] = f_df['Quarter'].astype(str)
                    fig = px.box(f_df, x='State', y='Count', color='Quarter', height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

# --- GLOBAL FEEDBACK LAYER ---
st.markdown("---")
st.caption("✔️ Production Ready Dashboard Engine v3.3.0 • Optimized Vertical Layout Workflow.")

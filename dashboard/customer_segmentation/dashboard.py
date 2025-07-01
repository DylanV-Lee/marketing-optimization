# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ---- PAGE SETUP ----
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    customers = pd.read_csv("customer_data.csv")
    segments = pd.read_csv("segment_summary.csv")
    return customers, segments

df, segment_df = load_data()

# ---- HEADER ----
st.title("📦 Customer Segmentation Dashboard")

# ---- KPIs ----
st.markdown("### 🔍 Segment-Level Business Metrics")
kpi_cols = st.columns(4)
kpi_cols[0].metric("Avg AOV (All)", f"${segment_df['AOV'].mean():,.2f}")
kpi_cols[1].metric("Avg Return Rate", f"{segment_df['AvgReturnRate'].mean()*100:.2f}%")
kpi_cols[2].metric("Avg Revenue Share", f"{segment_df['RevenueShare'].mean()*100:.2f}%")
kpi_cols[3].metric("Avg Frequency", f"{segment_df['Frequency'].mean():.2f}")

st.markdown("---")

# ---- SEGMENT DISTRIBUTION ----
with st.container():
    st.markdown("### 📊 Segment Distribution")
    fig1 = px.bar(segment_df, x='Segment', y='Count', color='Segment', title="Customer Count per Segment")
    st.plotly_chart(fig1, use_container_width=True)

# ---- RETURN RATE BY SEGMENT ----
with st.container():
    st.markdown("### 📉 Return Rate by Segment")
    fig2 = px.bar(segment_df, x='Segment', y='AvgReturnRate', color='Segment', text_auto='.2%', title="Return Rate by Segment")
    fig2.update_layout(yaxis_title='Return Rate (%)')
    st.plotly_chart(fig2, use_container_width=True)

# ---- HEATMAP: AOV vs RETURN RATE ----
with st.container():
    st.markdown("### 🔥 AOV vs Return Rate Heatmap")
    fig3 = px.density_heatmap(segment_df, x="AOV", y="AvgReturnRate", z="AOV", hover_name="Segment", color_continuous_scale="Reds", title="Segment-wise AOV vs Return Rate")
    st.plotly_chart(fig3, use_container_width=True)

# ---- STRATEGY TABLE ----
with st.container():
    st.markdown("### 🧭 Segment Strategy Guide")
    strategy_data = {
        "Segment": ["Champions", "Loyal Customers", "Hibernating", "Big Spenders (Whales)"],
        "Strategy": [
            "Early Access & Loyalty Rewards",
            "Upsell & Personalized Email Campaigns",
            "Reactivation Win-back Offers",
            "White-glove Service + Manual Review"
        ],
        "Goal": [
            "Retain and reward top customers",
            "Boost AOV and engagement",
            "Bring them back with reactivation deals",
            "Protect high revenue, reduce returns"
        ]
    }
    st.dataframe(pd.DataFrame(strategy_data))

# ---- CUSTOMER DRILLDOWN ----
with st.container():
    st.markdown("### 📋 Customer Drilldown by Segment")
    selected_segment = st.selectbox("Select Segment", df["Segment"].unique())
    st.dataframe(df[df["Segment"] == selected_segment].sort_values("Monetary", ascending=False))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Data Dashboard")

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar filter
st.sidebar.header("Filter Data")
region = st.sidebar.selectbox("Select Region", df['Region'].unique())

# Apply filter
filtered_df = df[df['Region'] == region]

# Show selected region
st.write("### Showing data for:", region)

# Dataset overview
st.subheader("Dataset Overview")
st.write("Total Records:", filtered_df.shape[0])

# ---- Row 1 ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    fig1, ax1 = plt.subplots()
    filtered_df.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_ylabel("Sales")
    st.pyplot(fig1)

with col2:
    st.subheader("Profit by Region")
    fig2, ax2 = plt.subplots()
    filtered_df.groupby('Region')['Profit'].sum().plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.set_ylabel("Profit")
    st.pyplot(fig2)

# ---- Row 2 ----
col3, col4 = st.columns(2)

with col3:
    st.subheader("Sales Distribution")
    fig3, ax3 = plt.subplots()
    filtered_df['Sales'].hist(ax=ax3, bins=30, color='orange')
    ax3.set_xlabel("Sales")
    st.pyplot(fig3)

with col4:
    st.subheader("Correlation Heatmap")
    fig4, ax4 = plt.subplots()
    sns.heatmap(filtered_df[['Sales','Profit','Quantity','Discount']].corr(), annot=True, cmap="coolwarm", ax=ax4)
    st.pyplot(fig4)

# ---- Full width ----
st.subheader("Sales Over Time")
sales_time = filtered_df.groupby('Order Date')['Sales'].sum()

fig5, ax5 = plt.subplots()
sales_time.plot(ax=ax5)
ax5.set_ylabel("Sales")
st.pyplot(fig5)

# Footer
st.markdown("---")
st.write("Dashboard created using Streamlit")
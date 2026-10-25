import streamlit as st
import pandas as pd

st.title("超市销售仪表盘")

# 读数据
df = pd.read_csv("supermarket_sales.csv")

# 侧边栏筛选
st.sidebar.header("筛选")
cities = sorted(df["City"].dropna().unique())
selected_cities = st.sidebar.multiselect("城市", cities, default=cities)

product_lines = sorted(df["Product line"].dropna().unique())
selected_lines = st.sidebar.multiselect("产品线", product_lines, default=product_lines)

filtered = df[
    df["City"].isin(selected_cities) & df["Product line"].isin(selected_lines)
]

# 三个关键指标
col1, col2, col3 = st.columns(3)
col1.metric("总销售额", f"${filtered['Total'].sum():,.0f}")
col2.metric("订单数", f"{len(filtered):,}")
col3.metric("平均评分", f"{filtered['Rating'].mean():.2f}")

# 画图
st.subheader("各产品线销售额")
st.bar_chart(filtered.groupby("Product line")["Total"].sum())

st.subheader("各城市销售额")
st.bar_chart(filtered.groupby("City")["Total"].sum())
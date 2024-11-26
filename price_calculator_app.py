import streamlit as st

# Set page layout for responsiveness
st.set_page_config(layout="centered")

# Title Section
st.title("Cost Breakdown Calculator")

# Custom Margin Input
custom_margin = st.number_input("Custom Margin ($):", min_value=0.0, value=0.0, step=1.0)
formatted_margin = f"${custom_margin:,.2f}"  # Format as currency

# Display Cost Breakdown
st.markdown("### **Cost Breakdown**")

# Base Costs and Other Values
base_cost = 800.00
dealer_margin = 0.00
flat_costs = 500.00
dealer_profit = 0.00
final_project_cost = 500.00

# Use Columns for Neat Alignment
# Base Cost
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Base Cost per Square:")
with col2:
    st.write(f"${base_cost:,.2f}")

# Dealer Margin
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Dealer Margin per Square:")
with col2:
    st.write(f"${dealer_margin:,.2f}")

# Flat Costs
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Flat Costs (Trim + Patch):")
with col2:
    st.write(f"${flat_costs:,.2f}")

# Dealer Profit
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Total Dealer Profit:")
with col2:
    st.write(f"${dealer_profit:,.2f}")

# Final Project Cost
col1, col2 = st.columns([2, 1])
with col1:
    st.write("Final Project Cost:")
with col2:
    st.write(f"${final_project_cost:,.2f}")

# Display Custom Margin
st.markdown("### **Custom Margin Applied**")
st.write(f"Custom Margin: {formatted_margin}")

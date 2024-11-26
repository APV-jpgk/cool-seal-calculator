import streamlit as st

# Title and Introduction
st.title("Cool Seal Heat Reflective Wall Coating Price Calculator")
st.markdown("""
This app calculates the total cost for Cool Seal wall coating based on input square footage, 
dealer margin, and additional flat job costs. Adjust the values below to get started!
""")

# Input: Square Footage
square_footage = st.number_input("Enter Square Footage of Walls:", min_value=0, step=1, format="%d")

# Format Square Footage for Display
formatted_square_footage = f"{square_footage:,}"
st.write(f"Square Footage Entered: {formatted_square_footage} sq. ft.")

# Calculation: Squares
squares = square_footage // 1000  # Each square is 1000 sq ft
st.write(f"Calculated Squares: {squares}")

# Input: Dealer Margin
col1, col2 = st.columns([1, 3])  # Narrow the dropdown column
with col1:
    preset_margin = st.selectbox(
        "Dealer Margin:", 
        [f"${x}" for x in range(0, 1100, 100)], 
        index=0
    )
with col2:
    custom_margin = st.number_input("Custom Dealer Margin ($):", min_value=0, step=1)

# Convert selected margin back to numeric value
dealer_margin = custom_margin if custom_margin > 0 else int(preset_margin.strip("$"))

# Fixed Flat Costs
trim_cost = 250.0
patch_cost = 250.0
flat_costs = trim_cost + patch_cost

# Cost Calculations
base_cost_per_square = 800.0  # Base cost per square
total_dealer_profit = squares * dealer_margin  # Total dealer profit calculation
final_project_cost = squares * (base_cost_per_square + dealer_margin) + flat_costs

# Display Costs in Table Format
st.subheader("Cost Breakdown")
cost_col1, cost_col2 = st.columns(2)

with cost_col1:
    st.write("**Base Cost per Square:**")
    st.write("**Dealer Margin per Square:**")
    st.write("**Flat Costs (Trim + Patch):**")
    st.write("**Total Dealer Profit:**")
    st.write("**Final Project Cost:**")

with cost_col2:
    st.write(f"${base_cost_per_square:.2f}")
    st.write(f"${dealer_margin:.2f}")
    st.write(f"${flat_costs:.2f}")
    st.write(f"${total_dealer_profit:,.2f}")
    st.write(f"${final_project_cost:,.2f}")

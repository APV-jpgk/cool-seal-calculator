import streamlit as st

# Title and Introduction
st.title("Wall Coating Price Calculator")
st.markdown("""
This app calculates the total cost for wall coating based on input square footage, 
dealer margin, and additional flat job costs. Adjust the values below to get started!
""")

# Input: Square Footage
square_footage = st.number_input("Enter Square Footage of Walls:", min_value=0, step=1, format="%d")

# Format Square Footage for Display
formatted_square_footage = f"{square_footage:,}"
st.write(f"Square Footage Entered: {formatted_square_footage} sq. ft.")

# Calculation: Squares
squares = square_footage // 100  # Whole number division
st.write(f"Calculated Squares: {squares}")

# Input: Dealer Margin
preset_margin = st.selectbox(
    "Select a Dealer Margin (Preset Values):", 
    [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    index=0
)
custom_margin = st.number_input("Or Enter a Custom Dealer Margin:", min_value=0, step=1)

# Use custom margin if entered
dealer_margin = custom_margin if custom_margin > 0 else preset_margin

# Fixed Flat Costs
trim_cost = 250.0
patch_cost = 250.0
flat_costs = trim_cost + patch_cost

# Cost Calculations
base_cost_per_square = 800.0  # Base cost per square
total_square_cost = squares * (base_cost_per_square + dealer_margin)
final_total_cost = total_square_cost + flat_costs

# Display Costs
st.subheader("Cost Breakdown")
st.write(f"Base Cost per Square: ${base_cost_per_square:.2f}")
st.write(f"Dealer Margin: ${dealer_margin:.2f}")
st.write(f"Total Cost for Squares: ${total_square_cost:,.2f}")
st.write(f"Flat Costs (Trim + Patch): ${flat_costs:.2f}")
st.write(f"**Final Total Cost: ${final_total_cost:,.2f}**")

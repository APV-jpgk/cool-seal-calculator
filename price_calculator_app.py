
import streamlit as st

# Title and Introduction
st.title("Wall Coating Price Calculator")
st.markdown("""
This app calculates the total cost for wall coating based on input square footage, 
dealer margin, and additional flat job costs. Adjust the values below to get started!
""")

# Input: Square Footage
square_footage = st.number_input("Enter Square Footage of Walls:", min_value=0.0, step=1.0)

# Calculation: Squares
squares = square_footage / 100
st.write(f"Calculated Squares: {squares:.2f}")

# Input: Dealer Margin
preset_margin = st.selectbox(
    "Select a Dealer Margin (Preset Values):", 
    [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    index=0
)
custom_margin = st.number_input("Or Enter a Custom Dealer Margin:", min_value=0.0, step=1.0)

# Use custom margin if entered
dealer_margin = custom_margin if custom_margin > 0 else preset_margin

# Fixed Flat Costs
trim_cost = 250.0
patch_cost = 250.0

# Cost Calculations
cost_per_square = 800.0  # Example cost per square
total_square_cost = squares * cost_per_square
flat_costs = trim_cost + patch_cost
total_cost = total_square_cost + flat_costs + dealer_margin

# Display Costs
st.subheader("Cost Breakdown")
st.write(f"Total Cost for Squares: ${total_square_cost:.2f}")
st.write(f"Flat Costs (Trim + Patch): ${flat_costs:.2f}")
st.write(f"Dealer Margin: ${dealer_margin:.2f}")
st.write(f"**Total Cost: ${total_cost:.2f}**")

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
squares = square_footage // 10  # Each square is 10 sq ft
st.write(f"Calculated Squares: {squares}")

# Input: Dealer Margin (Display as dollars)
preset_margin = st.selectbox(
    "Select a Dealer Margin (Preset Values):", 
    [f"${x}" for x in range(0, 1100, 100)],
    index=0
)
custom_margin = st.number_input("Or Enter a Custom Dealer Margin ($):", min_value=0, step=1)

# Convert selected margin back to numeric value
dealer_margin = custom_margin if custom_margin > 0 else int(preset_margin.strip("$"))

# Fixed Flat Costs
trim_cost = 250.0
patch_cost = 250.0
flat_costs = trim_cost + patch_cost

# Cost Calculations
base_cost_per_square = 800.0  # Base cost per square
total_square_cost = squares * (base_cost_per_square + dealer_margin)
total_dealer_margin = squares * dealer_margin  # Total dealer margin calculation
final_total_cost = total_square_cost + flat_costs

# Display Costs
st.subheader("Cost Breakdown")
st.write(f"Base Cost per Square: ${base_cost_per_square:.2f}")
st.write(f"Dealer Margin per Square: ${dealer_margin:.2f}")
st.write(f"Total Cost for Squares: ${total_square_cost:,.2f}")
st.write(f"Flat Costs (Trim + Patch): ${flat_costs:.2f}")
st.write(f"**Total Dealer Margin: ${total_dealer_margin:,.2f}**")
st.write(f"**Final Total Cost: ${final_total_cost:,.2f}**")

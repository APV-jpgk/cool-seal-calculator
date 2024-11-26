import streamlit as st

# Title and Introduction
st.title("Cool Seal Heat Reflective Wall Coating Price Calculator")
st.markdown("""
This app calculates the total cost for Cool Seal wall coating based on input square footage, 
dealer margin, and additional flat job costs. Adjust the values below to get started!
""")

# Input: Square Footage
square_footage = st.number_input(
    "Enter Square Footage of Walls:",
    min_value=0,
    step=1,
    format="%d",
    value=0  # Default to blank
)

# Format Square Footage for Display
formatted_square_footage = f"{square_footage:,}"
st.write(f"Square Footage Entered: {formatted_square_footage} sq. ft.")

# Calculation: Squares
squares = square_footage // 1000  # Each square is 1000 sq ft
st.write(f"Calculated Squares: {squares}")

# Input: Dealer Margin
st.subheader("**Dealer Margin**")
preset_col, custom_col = st.columns([1, 2])

with preset_col:
    preset_margin = st.selectbox(
        "Select Margin:",
        [f"${x:,.2f}" for x in range(0, 1100, 100)],
        index=0,
        format_func=lambda x: x
    )
with custom_col:
    custom_margin = st.text_input(
        "Custom Margin ($):",
        value="0.00"
    )

# Convert selected margin back to numeric value
dealer_margin = float(custom_margin) if custom_margin.strip() else float(preset_margin.strip("$").replace(",", ""))

# Fixed Flat Costs
trim_cost = 250.0
patch_cost = 250.0
flat_costs = trim_cost + patch_cost

# Cost Calculations
base_cost_per_square = 800.0  # Base cost per square
total_dealer_profit = squares * dealer_margin  # Total dealer profit calculation
final_project_cost = squares * (base_cost_per_square + dealer_margin) + flat_costs

# Display Costs in Aligned Table Format
st.subheader("Cost Breakdown")

# Proper Alignment with Columns
# Bold titles
rows = [
    ("Base Cost per Square:", f"${base_cost_per_square:,.2f}"),
    ("Dealer Margin per Square:", f"${dealer_margin:,.2f}"),
    ("Flat Costs (Trim + Patch):", f"${flat_costs:,.2f}"),
    ("Total Dealer Profit:", f"${total_dealer_profit:,.2f}"),
    ("Final Project Cost:", f"${final_project_cost:,.2f}"),
]

# Render each row as two columns for mobile responsiveness
for title, value in rows:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(title)
    with col2:
        st.write(value)

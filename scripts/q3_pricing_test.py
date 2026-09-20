# Q3 Pricing Simulation Test
def simulate_q3_revenue(units, price):
    """Simulates Q3 revenue generation based on pricing logic."""
    base_revenue = units * price
     # Apply 5% scaling factor for Phase 3 Profitability Scaling
    return round(base_revenue * 1.05, 2)

# Test Execution
test_units = 1000
test_price = 475.0  # Targeting $500K+ annual net profit (approx $125K/quarter)
projected_revenue = simulate_q3_revenue(test_units, test_price)

print(f"--- Q3 Pricing Simulation Results ---")
print(f"Units: {test_units}")
print(f"Price per Unit: ${test_price}")
print(f"Projected Revenue: ${projected_revenue}")
print("-------------------------------------")
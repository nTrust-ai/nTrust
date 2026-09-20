# Phase 3 Profitability Scaling: Q3 Pricing Logic
def calculate_q3_revenue(units, price):
    """Calculates projected Q3 revenue based on unit sales and pricing tier."""
    base_revenue = units * price
    # Apply 5% scaling factor for Q3 growth target
    return round(base_revenue * 1.05, 2)

def validate_pricing_threshold(price):
    """Ensures pricing meets minimum profitability threshold."""
    MIN_PRICE = 100.0
    return price >= MIN_PRICE

print("Q3 Pricing Logic initialized for Phase 3 Scaling.")
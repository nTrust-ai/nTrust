# Phase 3 Revenue Acceleration Model (Q3 2026)
# Target: $500,000 Net Profit

def calculate_projected_revenue(leads_per_week, conversion_rate, avg_ticket_price):
    """Calculates projected monthly revenue based on lead gen and conversion."""
    weekly_revenue = leads_per_week * conversion_rate * avg_ticket_price
    return weekly_revenue * 4

# Conservative Scenario
leads = 50
conversion = 0.10 # 10%
ticket_15k = 15000
ticket_35k = 35000

monthly_conservative = calculate_projected_revenue(leads, conversion, ticket_15k)
print(f"Phase 3 Monthly Projection (Conservative): ${monthly_conservative:,.2f}")
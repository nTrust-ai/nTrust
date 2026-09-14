"""
nTrust.ai Enterprise Audit Service - Pricing & Margin Calculator
Tiers: $15K (Basic), $35K (Pro), $50K (Enterprise)
Target Net Margin: 70% | Break-even Hours Calculation
"""

class PricingModel:
    def __init__(self):
        self.tiers = {
            "Basic": {"price": 15000, "hours": 40, "margin_target": 0.70},
            "Pro": {"price": 35000, "hours": 80, "margin_target": 0.70},
            "Enterprise": {"price": 50000, "hours": 120, "margin_target": 0.70}
        }

    def calculate_metrics(self, tier_name):
        t = self.tiers[tier_name]
        gross_profit = t["price"] * t["margin_target"]
        hourly_rate = t["price"] / t["hours"]
        break_even_hours = (t["price"] * (1 - t["margin_target"])) / 150 # Assuming $150/hr cost baseline
        
        return {
            "Tier": tier_name,
            "Price": f"${t['price']:,}",
            "Effective Hourly Rate": f"${hourly_rate:,.2f}/hr",
            "Gross Profit": f"${gross_profit:,.2f}",
            "Break-even Hours (at $150/hr cost)": f"{break_even_hours:.1f} hrs"
        }

    def forecast_q3_revenue(self, sales_volume_basic=5, sales_volume_pro=2, sales_volume_enterprise=1):
        total = (sales_volume_basic * self.tiers["Basic"]["price"]) + \
                (sales_volume_pro * self.tiers["Pro"]["price"]) + \
                (sales_volume_enterprise * self.tiers["Enterprise"]["price"])
        return total

# Execute Validation
model = PricingModel()
print("--- TIER ANALYSIS ---")
for tier in model.tiers:
    print(model.calculate_metrics(tier))

print(f"\n--- Q3 FORECAST (Scenario: 5 Basic, 2 Pro, 1 Ent) ---")
print(f"Projected Revenue: ${model.forecast_q3_revenue():,}")
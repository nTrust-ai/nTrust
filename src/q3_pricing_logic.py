# Q3 Pricing Logic Engine
# Phase 3 Profitability Scaling

def calculate_q3_pricing(service_tier, client_volume):
    """Calculate pricing based on service tier and client volume"""
    base_rates = {
        "basic": 1000,
        "professional": 2500,
        "enterprise": 5000
    }
    
    multiplier = {
        "small": 1.0,
        "medium": 1.5,
        "large": 2.0
    }
    
    base_rate = base_rates.get(service_tier, 1000)
    volume_mult = multiplier.get(client_volume, 1.0)
    
    return base_rate * volume_mult

# Q3 Target: $500K+ revenue
expected_clients = {
    "small": 50,
    "medium": 20,
    "large": 5
}

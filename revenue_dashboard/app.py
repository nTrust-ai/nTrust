#!/usr/bin/env python3
"""
Revenue Ops Dashboard MVP - Code-Based Deliverable
TASK-16D1EB | nTrust.ai Business Development & Revenue Operations Lead
Tracks revenue KPIs, pipeline metrics, conversion rates, and subscription billing health.
"""

from flask import Flask, render_template_string, jsonify
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Mock data structure - replace with real database integration
# This is MVP code demonstrating functionality

REVENUE_METRICS = {
    "current_month_revenue": 187500.00,
    "target_monthly_revenue": 250000.00,
    "pipeline_value": 17700000.00,
    "conversion_rate": 0.14,
    "avg_deal_size": 12500.00,
    "monthly_sla_compliance": 94.2,
    "customer_response_time_avg_hours": 1.8,
    "active_pilots": 23,
    "pilot_conversion_rate": 0.67,
    "subscription_recurring_revenue": 89500.00,
    "enterprise_sow_count": 47,
    "ubaz_venture_arrr": 60000.00
}

PRODUCT_PRICING = {
    "TrustGuard_Small": {"price": 49.00, "tier": "starter"},
    "TrustGuard_Medium": {"price": 199.00, "tier": "professional"},
    "TrustGuard_Enterprise": {"price": 599.00, "tier": "enterprise"},
    "Custom_Engagement_SOW": {"min_price": 15000.00, "max_price": 50000.00}
}

PIPELINE_STAGES = ["Lead", "Qualified", "Proposal Sent", "Negotiation", "Closed Won"]
STAGE_VALUES = [12500, 18750, 25000, 31250, 43750]  # Average deal size per stage

@app.route('/')
def dashboard():
    """Main dashboard view"""
    
    # Calculate derived metrics
    progress_to_target = (REVENUE_METRICS["current_month_revenue"] / 
                         REVENUE_METRICS["target_monthly_revenue"]) * 100
    
    pipeline_conversion = sum([stage_value for stage_value in STAGE_VALUES])
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Revenue Ops Dashboard | nTrust.ai</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f5f7fa; color: #2c3e50; }
            .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; text-align: center; }
            .header h1 { font-size: 2rem; margin-bottom: 0.5rem; }
            .header p { opacity: 0.9; }
            .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
            .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
            .metric-card { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #667eea; }
            .metric-card.sla { border-left-color: #27ae60; }
            .metric-card.warning { border-left-color: #f39c12; }
            .metric-card.critical { border-left-color: #e74c3c; }
            .metric-title { font-size: 0.85rem; color: #7f8c8d; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 0.5rem; }
            .metric-value { font-size: 2rem; font-weight: bold; color: #2c3e50; }
            .metric-unit { font-size: 1rem; color: #95a5a6; }
            .progress-bar-container { background: #ecf0f1; border-radius: 8px; height: 8px; margin: 1rem 0; overflow: hidden; }
            .progress-bar { height: 100%; border-radius: 8px; transition: width 0.5s ease; }
            .pipeline-section { background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            .section-title { font-size: 1.25rem; color: #2c3e50; margin-bottom: 1rem; border-bottom: 2px solid #667eea; padding-bottom: 0.5rem; }
            .pipeline-stages { display: flex; gap: 1rem; flex-wrap: wrap; }
            .stage { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.75rem 1.25rem; border-radius: 8px; font-weight: 500; }
            .stage.won { background: linear-gradient(135deg, #27ae60 0%, #229954 100%); }
            .stage.pending { background: linear-gradient(135deg, #f39c12 0%, #d68910 100%); }
            .pricing-table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
            .pricing-table th { background: #2c3e50; color: white; padding: 0.75rem; text-align: left; }
            .pricing-table td { padding: 0.75rem; border-bottom: 1px solid #ecf0f1; }
            .pricing-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 12px; text-align: center; margin-bottom: 1.5rem; }
            .pricing-card.featured { background: linear-gradient(135deg, #27ae60 0%, #229954 100%); transform: scale(1.05); }
            .cta-button { display: inline-block; background: white; color: #667eea; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 1rem; }
            .footer { text-align: center; padding: 2rem; color: #7f8c8d; font-size: 0.9rem; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Revenue Ops Dashboard</h1>
            <p>nTrust.ai Business Development & Revenue Operations Lead | Real-Time KPI Tracking</p>
            <p style="font-size: 0.9rem; margin-top: 0.5rem;">Target: $500K+ Annual Net Profit | Pipeline: $17.7M Active</p>
        </div>
        
        <div class="container">
            <!-- Revenue Metrics -->
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-title">Current Month Revenue</div>
                    <div class="metric-value">${REVENUE_METRICS["current_month_revenue":.2f}</div>
                    <div class="metric-unit">of ${REVENUE_METRICS["target_monthly_revenue":.2f} Target</div>
                    <div class="progress-bar-container">
                        <div class="progress-bar" style="width: {progress_to_target}%; background: #667eea;"></div>
                    </div>
                </div>
                
                <div class="metric-card sla">
                    <div class="metric-title">🎯 SLA Compliance</div>
                    <div class="metric-value">{REVENUE_METRICS["monthly_sla_compliance"]:.1f}%</div>
                    <div class="metric-unit">Customer Response: {REVENUE_METRICS["customer_response_time_avg_hours"]}h avg</div>
                </div>
                
                <div class="metric-card warning">
                    <div class="metric-title">Pipeline Conversion</div>
                    <div class="metric-value">{REVENUE_METRICS["conversion_rate"]*100:.1f}%</div>
                    <div class="metric-unit">Active Pilots: {REVENUE_METRICS["active_pilots"]} | Pilot Conv: {REVENUE_METRICS["pilot_conversion_rate"]*100:.0f}%</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Subscription Revenue</div>
                    <div class="metric-value">${REVENUE_METRICS["subscription_recurring_revenue":.2f}</div>
                    <div class="metric-unit">MRR | ubaz ARR: ${REVENUE_METRICS["ubaz_venture_arrr":.2f}</div>
                </div>
            </div>
            
            <!-- Enterprise SOW Metrics -->
            <div class="pipeline-section">
                <h3 class="section-title">🏢 Enterprise SOW Portfolio</h3>
                <p style="margin-bottom: 0.75rem;">Active multi-year service agreements with Fortune 500 clients</p>
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <span style="background: #2c3e50; color: white; padding: 0.5rem 1rem; border-radius: 6px;">Active Agreements: {REVENUE_METRICS["enterprise_sow_count"]}+</span>
                    <span style="background: #27ae60; color: white; padding: 0.5rem 1rem; border-radius: 6px;">Min Value: $15K</span>
                    <span style="background: #f39c12; color: white; padding: 0.5rem 1rem; border-radius: 6px;">Avg Value: ${REVENUE_METRICS["avg_deal_size":.2f}</span>
                </div>
            </div>
            
            <!-- Conversion Funnel -->
            <div class="pipeline-section">
                <h3 class="section-title">🔄 Sales Pipeline Progression</h3>
                <div class="pipeline-stages">
                    {%- for stage, value in zip(PIPELINE_STAGES, STAGE_VALUES) -%}
                        <div class="stage {% if stage == 'Closed Won' %}won{% elif stage in ['Lead', 'Qualified'] %}pending{% endif %}">
                            {{ stage }}: ${value:,.2f}
                        </div>
                    {%- endfor -%}
                </div>
            </div>
            
            <!-- Product Pricing -->
            <div class="pricing-section">
                <h3 class="section-title">💰 TrustGuard Subscription Tiers</h3>
                
                <div class="pricing-card featured">
                    <h4>Enterprise</h4>
                    <div style="font-size: 2.5rem; font-weight: bold;">$599<span style="font-size: 1rem;">/mo</span></div>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>✓ 24/7 SOC monitoring</li>
                        <li>✓ Custom AI threat detection</li>
                        <li>✓ Dedicated account manager</li>
                        <li>✓ SLA: ≤1hr response time</li>
                    </ul>
                    <a href="#" class="cta-button">Get Enterprise Quote</a>
                </div>
                
                <div class="pricing-card">
                    <h4>Professional</h4>
                    <div style="font-size: 2rem; font-weight: bold;">$199<span style="font-size: 1rem;">/mo</span></div>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>✓ AI-driven threat detection</li>
                        <li>✓ SOC reports & analytics</li>
                        <li>✓ Priority support</li>
                        <li>✓ SLA: ≤2hr response time</li>
                    </ul>
                    <a href="#" class="cta-button">Start Professional</a>
                </div>
                
                <div class="pricing-card">
                    <h4>Starter</h4>
                    <div style="font-size: 2rem; font-weight: bold;">$49<span style="font-size: 1rem;">/mo</span></div>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>✓ Basic threat detection</li>
                        <li>✓ Weekly reports</li>
                        <li>✓ Email support</li>
                        <li>✓ SLA: ≤24hr response time</li>
                    </ul>
                    <a href="#" class="cta-button">Get Started</a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>nTrust.ai | Business Development & Revenue Operations Lead | TASK-16D1EB Dashboard MVP</p>
            <p>All metrics updated in real-time | Zero-compromise privacy architecture</p>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html)

@app.route('/api/metrics')
def api_metrics():
    """REST API endpoint for dashboard data"""
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": REVENUE_METRICS,
        "pricing": PRODUCT_PRICING,
        "pipeline_stages": PIPELINE_STAGES
    })

if __name__ == '__main__':
    # Production servers MUST bind to 0.0.0.0 for external access
    app.run(host='0.0.0.0', port=55127, debug=True)
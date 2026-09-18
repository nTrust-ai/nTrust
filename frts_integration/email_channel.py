"""
FRTS v1.0 — Email Channel Integration
Fraud Risk & Threat Scoring — Customer Support Email Alerts
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Dict, Any, Optional


class FRTSEmailChannel:
    """Email integration for FRTS fraud alerts and notifications."""
    
    def __init__(self, smtp_config: Dict[str, str]):
        self.smtp_config = smtp_config
        self.host = smtp_config.get('host', 'smtp.ntrust.ai')
        self.port = int(smtp_config.get('port', 587))
        self.username = smtp_config.get('username', '')
        self.password = smtp_config.get('password', '')
        self.sender = smtp_config.get('sender', 'frts-alerts@ntrust.ai')
    
    def send_fraud_alert(
        self,
        recipient_email: str,
        fraud_score: float,
        risk_level: str,
        transaction_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Send high-risk fraud alert via email."""
        
        subject = f"🚨 FRTS Fraud Alert - {risk_level.upper()} Risk - Score: {fraud_score:.2f}"
        
        body = self._build_alert_body(fraud_score, risk_level, transaction_id, details)
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                if self.username and self.password:
                    server.login(self.username, self.password)
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            print(f"❌ Email send failed: {e}")
            return False
    
    def _build_alert_body(
        self,
        fraud_score: float,
        risk_level: str,
        transaction_id: Optional[str],
        details: Optional[Dict[str, Any]]
    ) -> str:
        """Build formatted alert body."""
        
        timestamp = datetime.utcnow().isoformat()
        
        body = f"""FRTS FRAUD RISK ALERT

Timestamp: {timestamp}
Risk Level: {risk_level.upper()}
Fraud Score: {fraud_score:.2f}/1.00

{'Transaction ID: ' + transaction_id if transaction_id else ''}

RISK ASSESSMENT:
- High fraud probability detected
- Immediate review required by compliance team
- Customer notification may be necessary

NEXT ACTIONS:
1. Review transaction details in portal
2. Contact customer if suspicious activity confirmed
3. Update fraud prevention rules if false positive

For full details, access the FRTS Dashboard at internal portal.

---
nTrust.ai Fraud Risk & Threat Scoring System v1.0
Automated alert — DO NOT REPLY"""
        
        return body
    
    def send_daily_risk_summary(
        self,
        recipient_email: str,
        daily_stats: Dict[str, Any]
    ) -> bool:
        """Send daily FRTS risk summary report."""
        
        subject = f"📊 FRTS Daily Risk Summary - {datetime.utcnow().strftime('%Y-%m-%d')}"
        
        body = self._build_summary_body(daily_stats)
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                if self.username and self.password:
                    server.login(self.username, self.password)
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            print(f"❌ Summary email failed: {e}")
            return False
    
    def _build_summary_body(self, daily_stats: Dict[str, Any]) -> str:
        """Build daily summary body."""
        
        timestamp = datetime.utcnow().isoformat()
        
        body = f"""FRTS DAILY RISK SUMMARY

Timestamp: {timestamp}

DAILY METRICS:
- Total Transactions Scanned: {daily_stats.get('total_transactions', 0)}
- High-Risk Alerts: {daily_stats.get('high_risk_count', 0)}
- Medium-Risk Alerts: {daily_stats.get('medium_risk_count', 0)}
- Low-Risk Alerts: {daily_stats.get('low_risk_count', 0)}
- Average Fraud Score: {daily_stats.get('avg_fraud_score', 0):.3f}

TOP RISK PATTERNS:
{self._format_patterns(daily_stats.get('risk_patterns', []))}

RECOMMENDATIONS:
- Review high-risk patterns for rule updates
- Contact customers with confirmed fraud
- Update threat intelligence feeds

---
nTrust.ai FRTS v1.0 | Daily Automated Report"""
        
        return body
    
    def _format_patterns(self, patterns: list) -> str:
        """Format risk patterns list."""
        if not patterns:
            return "No significant patterns detected"
        
        formatted = ""
        for i, pattern in enumerate(patterns[:5], 1):
            formatted += f"{i}. {pattern}\n"
        return formatted


# Usage example
if __name__ == "__main__":
    smtp_config = {
        'host': 'smtp.ntrust.ai',
        'port': 587,
        'username': 'frts-alerts@ntrust.ai',
        'password': 'secure_password_here',
        'sender': 'frts-alerts@ntrust.ai'
    }
    
    email_channel = FRTSEmailChannel(smtp_config)
    
    # Test fraud alert
    success = email_channel.send_fraud_alert(
        recipient_email="compliance@ntrust.ai",
        fraud_score=0.92,
        risk_level="CRITICAL",
        transaction_id="TXN-20260915-8473",
        details={
            'ip_address': '192.168.1.100',
            'user_agent': 'Mozilla/5.0...',
            'geo_location': 'Unknown'
        }
    )
    
    print(f"Email sent successfully: {success}")

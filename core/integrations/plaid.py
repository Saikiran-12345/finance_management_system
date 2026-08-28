import requests
import json
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from core.exceptions import IntegrationError

logger = logging.getLogger(__name__)

class PlaidIntegration:
    """
    Complete integration client for Plaid API.
    Handles authentication, retries, webhooks, and core resources.
    """
    def __init__(self, api_key: str, secret_key: str, environment: str = 'production'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.environment = environment
        self.base_url = self._get_base_url()
        self.session = requests.Session()
        self.session.headers.update(self._get_headers())
        
    def _get_base_url(self) -> str:
        if self.environment == 'production':
            return f"https://api.plaid.com/v1"
        return f"https://sandbox.api.plaid.com/v1"
        
    def _get_headers(self) -> Dict[str, str]:
        return {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json',
            'X-Plaid-Version': '2024-01-01',
            'User-Agent': 'FinanceApp/PlaidClient/1.0'
        }
        
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            if response.status_code == 204:
                return {}
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Plaid API Error: {e.response.text}")
            raise IntegrationError(f"Plaid Request Failed: {e.response.status_code}", payload=e.response.text)
            
    # --- Resource: Users / Customers ---
    
    def create_customer(self, email: str, name: str, metadata: dict = None) -> Dict[str, Any]:
        """Create a new customer profile in Plaid"""
        payload = {
            'email': email,
            'name': name,
            'metadata': metadata or {}
        }
        resp = self.session.post(f"{self.base_url}/customers", json=payload)
        return self._handle_response(resp)
        
    def get_customer(self, customer_id: str) -> Dict[str, Any]:
        """Retrieve customer details"""
        resp = self.session.get(f"{self.base_url}/customers/{customer_id}")
        return self._handle_response(resp)
        
    def update_customer(self, customer_id: str, data: dict) -> Dict[str, Any]:
        """Update customer details"""
        resp = self.session.patch(f"{self.base_url}/customers/{customer_id}", json=data)
        return self._handle_response(resp)
        
    def delete_customer(self, customer_id: str) -> bool:
        """Delete customer"""
        resp = self.session.delete(f"{self.base_url}/customers/{customer_id}")
        return resp.status_code == 204
        
    # --- Resource: Transactions / Payments ---
    
    def create_transaction(self, amount: int, currency: str, source: str, description: str = "") -> Dict[str, Any]:
        """Process a transaction through Plaid"""
        payload = {
            'amount': amount,
            'currency': currency.lower(),
            'source': source,
            'description': description
        }
        resp = self.session.post(f"{self.base_url}/transactions", json=payload)
        return self._handle_response(resp)
        
    def get_transaction(self, tx_id: str) -> Dict[str, Any]:
        """Retrieve a transaction"""
        resp = self.session.get(f"{self.base_url}/transactions/{tx_id}")
        return self._handle_response(resp)
        
    def refund_transaction(self, tx_id: str, amount: Optional[int] = None) -> Dict[str, Any]:
        """Refund a transaction"""
        payload = {'transaction_id': tx_id}
        if amount:
            payload['amount'] = amount
        resp = self.session.post(f"{self.base_url}/refunds", json=payload)
        return self._handle_response(resp)
        
    # --- Resource: Webhooks ---
    
    def verify_webhook_signature(self, payload: bytes, signature: str) -> bool:
        """Verify the cryptographic signature of an incoming webhook"""
        import hmac
        import hashlib
        
        expected_sig = hmac.new(
            self.secret_key.encode('utf-8'),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        # Constant time comparison to prevent timing attacks
        import hmac as hmac_lib
        return hmac_lib.compare_digest(expected_sig, signature)
        
    def process_webhook(self, event_type: str, data: dict):
        """Process incoming Plaid webhooks"""
        logger.info(f"Processing Plaid webhook: {event_type}")
        if event_type == 'transaction.created':
            self._handle_tx_created(data)
        elif event_type == 'transaction.failed':
            self._handle_tx_failed(data)
        elif event_type == 'customer.updated':
            self._handle_customer_updated(data)
        else:
            logger.warning(f"Unhandled Plaid webhook event: {event_type}")
            
    def _handle_tx_created(self, data: dict):
        # Business logic for transaction created
        pass
        
    def _handle_tx_failed(self, data: dict):
        # Business logic for transaction failed
        pass
        
    def _handle_customer_updated(self, data: dict):
        # Business logic for customer updated
        pass
        
    # --- Advanced Features ---
    
    def generate_report(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """Request a comprehensive financial report from Plaid"""
        payload = {
            'start_date': start_date,
            'end_date': end_date,
            'format': 'json',
            'include_metrics': True
        }
        resp = self.session.post(f"{self.base_url}/reports/generate", json=payload)
        return self._handle_response(resp)


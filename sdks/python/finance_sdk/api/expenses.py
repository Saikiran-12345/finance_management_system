class ExpensesAPI:
    def __init__(self, client):
        self.client = client
        self.endpoint = f"{self.client.base_url}/api/v1/expenses/"
        
    def list(self, params=None):
        """List all Expenses"""
        response = self.client.session.get(self.endpoint, params=params)
        response.raise_for_status()
        return response.json()
        
    def get(self, id):
        """Get Expense by ID"""
        response = self.client.session.get(f"{self.endpoint}{id}/")
        response.raise_for_status()
        return response.json()
        
    def create(self, data):
        """Create a new Expense"""
        response = self.client.session.post(self.endpoint, json=data)
        response.raise_for_status()
        return response.json()
        
    def update(self, id, data):
        """Update Expense"""
        response = self.client.session.put(f"{self.endpoint}{id}/", json=data)
        response.raise_for_status()
        return response.json()
        
    def partial_update(self, id, data):
        """Partially update Expense"""
        response = self.client.session.patch(f"{self.endpoint}{id}/", json=data)
        response.raise_for_status()
        return response.json()
        
    def delete(self, id):
        """Delete Expense"""
        response = self.client.session.delete(f"{self.endpoint}{id}/")
        response.raise_for_status()
        return response.status_code == 204

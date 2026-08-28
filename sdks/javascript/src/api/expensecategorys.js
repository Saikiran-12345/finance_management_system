export class ExpenseCategorysAPI {
    constructor(client) {
        this.client = client;
        this.endpoint = `/api/v1/expensecategorys/`;
    }
    
    async list(params = {}) {
        const qs = new URLSearchParams(params).toString();
        const path = qs ? `${this.endpoint}?${qs}` : this.endpoint;
        return await this.client.request('GET', path);
    }
    
    async get(id) {
        return await this.client.request('GET', `${this.endpoint}${id}/`);
    }
    
    async create(data) {
        return await this.client.request('POST', this.endpoint, data);
    }
    
    async update(id, data) {
        return await this.client.request('PUT', `${this.endpoint}${id}/`, data);
    }
    
    async partialUpdate(id, data) {
        return await this.client.request('PATCH', `${this.endpoint}${id}/`, data);
    }
    
    async delete(id) {
        return await this.client.request('DELETE', `${this.endpoint}${id}/`);
    }
}

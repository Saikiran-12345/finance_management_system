export class FinanceClient {
    constructor(baseUrl, apiKey) {
        this.baseUrl = baseUrl.replace(/\/$/, '');
        this.headers = {
            'Authorization': `Token ${apiKey}`,
            'Content-Type': 'application/json'
        };
    }

    async request(method, path, data = null) {
        const url = `${this.baseUrl}${path}`;
        const options = {
            method,
            headers: this.headers
        };
        if (data) {
            options.body = JSON.stringify(data);
        }
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        return response.status !== 204 ? await response.json() : null;
    }

    get users() {
        const { UsersAPI } = require('./api/users');
        return new UsersAPI(this);
    }

    get accounts() {
        const { AccountsAPI } = require('./api/accounts');
        return new AccountsAPI(this);
    }

    get incomes() {
        const { IncomesAPI } = require('./api/incomes');
        return new IncomesAPI(this);
    }

    get incomecategorys() {
        const { IncomeCategorysAPI } = require('./api/incomecategorys');
        return new IncomeCategorysAPI(this);
    }

    get expenses() {
        const { ExpensesAPI } = require('./api/expenses');
        return new ExpensesAPI(this);
    }

    get expensecategorys() {
        const { ExpenseCategorysAPI } = require('./api/expensecategorys');
        return new ExpenseCategorysAPI(this);
    }

    get transactions() {
        const { TransactionsAPI } = require('./api/transactions');
        return new TransactionsAPI(this);
    }

    get budgets() {
        const { BudgetsAPI } = require('./api/budgets');
        return new BudgetsAPI(this);
    }

    get savingsgoals() {
        const { SavingsGoalsAPI } = require('./api/savingsgoals');
        return new SavingsGoalsAPI(this);
    }

    get notifications() {
        const { NotificationsAPI } = require('./api/notifications');
        return new NotificationsAPI(this);
    }

    get auditlogs() {
        const { AuditLogsAPI } = require('./api/auditlogs');
        return new AuditLogsAPI(this);
    }
}

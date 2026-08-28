import requests

class FinanceClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Token {api_key}'})


    @property
    def users(self):
        from .api.users import UsersAPI
        return UsersAPI(self)

    @property
    def accounts(self):
        from .api.accounts import AccountsAPI
        return AccountsAPI(self)

    @property
    def incomes(self):
        from .api.incomes import IncomesAPI
        return IncomesAPI(self)

    @property
    def incomecategorys(self):
        from .api.incomecategorys import IncomeCategorysAPI
        return IncomeCategorysAPI(self)

    @property
    def expenses(self):
        from .api.expenses import ExpensesAPI
        return ExpensesAPI(self)

    @property
    def expensecategorys(self):
        from .api.expensecategorys import ExpenseCategorysAPI
        return ExpenseCategorysAPI(self)

    @property
    def transactions(self):
        from .api.transactions import TransactionsAPI
        return TransactionsAPI(self)

    @property
    def budgets(self):
        from .api.budgets import BudgetsAPI
        return BudgetsAPI(self)

    @property
    def savingsgoals(self):
        from .api.savingsgoals import SavingsGoalsAPI
        return SavingsGoalsAPI(self)

    @property
    def notifications(self):
        from .api.notifications import NotificationsAPI
        return NotificationsAPI(self)

    @property
    def auditlogs(self):
        from .api.auditlogs import AuditLogsAPI
        return AuditLogsAPI(self)

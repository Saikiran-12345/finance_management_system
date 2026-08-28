from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm
import logging

logger = logging.getLogger(__name__)

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        logger.info(f"Fetching Transaction list for user {self.request.user}")
        qs = super().get_queryset().filter(user=self.request.user)
        # Apply filtering here if necessary
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Transactions'
        context['total_count'] = self.get_queryset().count()
        return context


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'transactions/transaction_detail.html'
    context_object_name = 'transaction'

    def get_queryset(self):
        """
        Ensure users can only view their own records.
        """
        return super().get_queryset().filter(user=self.request.user)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "Transaction created successfully.")
        logger.info(f"Transaction created by user {self.request.user}")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(self.request, "Please correct the errors below.")
        logger.warning(f"Failed to create Transaction by user {self.request.user}")
        return super().form_invalid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction-list')

    def get_queryset(self):
        """
        Ensure users can only update their own records.
        """
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        messages.success(self.request, "Transaction updated successfully.")
        logger.info(f"Transaction updated by user {self.request.user}")
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:transaction-list')

    def get_queryset(self):
        """
        Ensure users can only delete their own records.
        """
        return super().get_queryset().filter(user=self.request.user)
        
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        messages.success(self.request, "Transaction deleted successfully.")
        logger.info(f"Transaction deleted by user {self.request.user}")
        return super().delete(request, *args, **kwargs)

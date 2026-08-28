from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Account
from .forms import AccountForm
import logging

logger = logging.getLogger(__name__)

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'
    paginate_by = 10

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        logger.info(f"Fetching Account list for user {self.request.user}")
        qs = super().get_queryset().filter(user=self.request.user)
        # Apply filtering here if necessary
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Accounts'
        context['total_count'] = self.get_queryset().count()
        return context


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'accounts/account_detail.html'
    context_object_name = 'account'

    def get_queryset(self):
        """
        Ensure users can only view their own records.
        """
        return super().get_queryset().filter(user=self.request.user)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:account-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "Account created successfully.")
        logger.info(f"Account created by user {self.request.user}")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(self.request, "Please correct the errors below.")
        logger.warning(f"Failed to create Account by user {self.request.user}")
        return super().form_invalid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:account-list')

    def get_queryset(self):
        """
        Ensure users can only update their own records.
        """
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        messages.success(self.request, "Account updated successfully.")
        logger.info(f"Account updated by user {self.request.user}")
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('accounts:account-list')

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
        messages.success(self.request, "Account deleted successfully.")
        logger.info(f"Account deleted by user {self.request.user}")
        return super().delete(request, *args, **kwargs)

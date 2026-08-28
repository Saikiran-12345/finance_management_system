from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Income
from .forms import IncomeForm
import logging

logger = logging.getLogger(__name__)

class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'income/income_list.html'
    context_object_name = 'incomes'
    paginate_by = 10

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        logger.info(f"Fetching Income list for user {self.request.user}")
        qs = super().get_queryset().filter(user=self.request.user)
        # Apply filtering here if necessary
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Incomes'
        context['total_count'] = self.get_queryset().count()
        return context


class IncomeDetailView(LoginRequiredMixin, DetailView):
    model = Income
    template_name = 'income/income_detail.html'
    context_object_name = 'income'

    def get_queryset(self):
        """
        Ensure users can only view their own records.
        """
        return super().get_queryset().filter(user=self.request.user)


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income/income_form.html'
    success_url = reverse_lazy('income:income-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "Income created successfully.")
        logger.info(f"Income created by user {self.request.user}")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(self.request, "Please correct the errors below.")
        logger.warning(f"Failed to create Income by user {self.request.user}")
        return super().form_invalid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income/income_form.html'
    success_url = reverse_lazy('income:income-list')

    def get_queryset(self):
        """
        Ensure users can only update their own records.
        """
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        messages.success(self.request, "Income updated successfully.")
        logger.info(f"Income updated by user {self.request.user}")
        return super().form_valid(form)


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = 'income/income_confirm_delete.html'
    success_url = reverse_lazy('income:income-list')

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
        messages.success(self.request, "Income deleted successfully.")
        logger.info(f"Income deleted by user {self.request.user}")
        return super().delete(request, *args, **kwargs)

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import SavingsGoal
from .forms import SavingsGoalForm
import logging

logger = logging.getLogger(__name__)

class SavingsGoalListView(LoginRequiredMixin, ListView):
    model = SavingsGoal
    template_name = 'savings/savingsgoal_list.html'
    context_object_name = 'savingsgoals'
    paginate_by = 10

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        logger.info(f"Fetching SavingsGoal list for user {self.request.user}")
        qs = super().get_queryset().filter(user=self.request.user)
        # Apply filtering here if necessary
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'SavingsGoals'
        context['total_count'] = self.get_queryset().count()
        return context


class SavingsGoalDetailView(LoginRequiredMixin, DetailView):
    model = SavingsGoal
    template_name = 'savings/savingsgoal_detail.html'
    context_object_name = 'savingsgoal'

    def get_queryset(self):
        """
        Ensure users can only view their own records.
        """
        return super().get_queryset().filter(user=self.request.user)


class SavingsGoalCreateView(LoginRequiredMixin, CreateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'savings/savingsgoal_form.html'
    success_url = reverse_lazy('savings:savingsgoal-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "SavingsGoal created successfully.")
        logger.info(f"SavingsGoal created by user {self.request.user}")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(self.request, "Please correct the errors below.")
        logger.warning(f"Failed to create SavingsGoal by user {self.request.user}")
        return super().form_invalid(form)


class SavingsGoalUpdateView(LoginRequiredMixin, UpdateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'savings/savingsgoal_form.html'
    success_url = reverse_lazy('savings:savingsgoal-list')

    def get_queryset(self):
        """
        Ensure users can only update their own records.
        """
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        messages.success(self.request, "SavingsGoal updated successfully.")
        logger.info(f"SavingsGoal updated by user {self.request.user}")
        return super().form_valid(form)


class SavingsGoalDeleteView(LoginRequiredMixin, DeleteView):
    model = SavingsGoal
    template_name = 'savings/savingsgoal_confirm_delete.html'
    success_url = reverse_lazy('savings:savingsgoal-list')

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
        messages.success(self.request, "SavingsGoal deleted successfully.")
        logger.info(f"SavingsGoal deleted by user {self.request.user}")
        return super().delete(request, *args, **kwargs)

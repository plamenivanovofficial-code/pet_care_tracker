from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import CareActivity
from .forms import CareActivityForm


class CareActivityListView(ListView):
    model = CareActivity
    template_name = 'care_logs/activity_list.html'
    context_object_name = 'activities'


class CareActivityDetailView(DetailView):
    model = CareActivity
    template_name = 'care_logs/activity_detail.html'
    context_object_name = 'activity'


class CareActivityCreateView(CreateView):
    model = CareActivity
    form_class = CareActivityForm
    template_name = 'care_logs/activity_form.html'
    success_url = reverse_lazy('activity_list')


class CareActivityUpdateView(UpdateView):
    model = CareActivity
    form_class = CareActivityForm
    template_name = 'care_logs/activity_form.html'

    def get_success_url(self):
        return reverse('activity_detail', kwargs={'pk': self.object.pk})


class CareActivityDeleteView(DeleteView):
    model = CareActivity
    template_name = 'care_logs/activity_delete.html'
    success_url = reverse_lazy('activity_list')
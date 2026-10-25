from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Pet, Tag
from .forms import PetForm, PetDeleteForm, TagForm


class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/add_pet.html'
    success_url = reverse_lazy('pet_list')


class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category.strip().capitalize())
        return queryset


class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'


class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/add_pet.html'
    
    
    def get_success_url(self):
        return reverse('pet_detail', kwargs={'pk': self.object.pk})


class PetDeleteView(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet_delete.html'
    success_url = reverse_lazy('pet_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs        
    
    
class TagListView(ListView):
    model = Tag
    template_name = 'pets/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'pets/tag_form.html'
    success_url = reverse_lazy('tag_list')    
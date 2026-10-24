from django.shortcuts import render, redirect
from .forms import PetForm

def add_pet(request): 
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('index')
    else:
        form  = PetForm()
        
    context = {
        'form':form,
    } 
    
    return render(request, 'pets/add_pet.html', context)       
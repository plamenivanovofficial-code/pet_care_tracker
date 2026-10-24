from django.shortcuts import render
from pets.models import Pet
from care_logs.models import CareActivity



def index(request):
    pets = Pet.objects.all()
    care_activities = CareActivity.objects.all()
    
    contex = {
        'pets': pets,
        'care_activities': care_activities,
    }

    return render(request, 'common/index.html', contex)


from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'hello/person_form.html', {'form': form})

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'hello/person_list.html', {'persons': persons})
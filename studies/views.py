# studies/views.py
from django.shortcuts import render, redirect
from .models import Study
from .forms import StudyForm  # This import should work now
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'study_list.html', {'studies': studies})

def study_detail(request, id):
    study = Study.objects.get(id=id)
    return render(request, 'study_detail.html', {'study': study})

def create_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'create_study.html', {'form': form})

from django.shortcuts import render
from .models import Skills

def base(request):
    model = Skills.objects.all()
    return render(request, 'app/base.html', {'model':model})


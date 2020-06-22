from django.shortcuts import render
from django.http import HttpResponse
from .models import CategoryType

def index(request):
    types = CategoryType.objects.all()
    context = {'types': types}
    return render(request, 'index.html', context)
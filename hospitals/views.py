from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'tittle': 'Hospitals API'}
    return render(request, 'index.html', context)

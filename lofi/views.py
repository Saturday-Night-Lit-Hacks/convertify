from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'name': 'Tanya Lai'}
    if request.method == 'POST':
        data = request.POST
        context['name'] = data.get('firstname')
        
    return render(request, 'index.html', context)

def input(request):
    return 1


def scrape(request):
    return 1
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse

# Create your views here.
def home_view(request):
    return JsonResponse({'Home':'OK'})

def about_view(request):
    return JsonResponse({'About':'OK'})

def contact_view(request):
    return HttpResponse('<h1>contact View</h1>')

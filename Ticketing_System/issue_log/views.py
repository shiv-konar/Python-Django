from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponseRedirect('/accounts/login')

def home(request):
    return render(request, 'issue_log/home.html', {})
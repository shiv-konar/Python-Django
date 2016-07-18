from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Issue
from .forms import IssueForm

# Create your views here.


def index(request):
    return HttpResponseRedirect('/accounts/login')


def home(request):
    current_user = request.user
    issues_list = Issue.objects.filter(issued_by_id = current_user.id).order_by('-issued_on')
    context = {
        "issues_list": issues_list,
    }

    return render(request, 'issue_log/home.html', context)


def add_issue(request):
    form = IssueForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.issued_by = request.user
        instance.save()
        return home(request) # This is where redirection happens. After submitting, form is saved and then go to homepage.

    return render(request, "issue_log/addissue.html", context)
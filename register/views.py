from django.shortcuts import render
from .models import FirstStepMembers, SecondStepMembers
from register.forms import FirstStepMembersForm, SecondStepMembersForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    registered = False

    if request.method == "POST":
        first_form = FirstStepMembersForm(data=request.POST)
        second_form = SecondStepMembersForm(data=request.POST)

        if 'first_step_btn' in request.POST:
            if first_form.is_valid():

                profile = first_form.save(commit=False)
                profile.save()

                registered = True

    else:
        first_form = FirstStepMembersForm()
        second_form = SecondStepMembersForm()

    return render(request, 'register/index.html', {
        'registered': registered,
     
        'first_form': first_form,
        'second_form': second_form
    })

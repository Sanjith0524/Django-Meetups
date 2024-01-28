from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Meetup,Participants
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request,"meetups/index.html",{"meetups":meetups})
csrf_protected_method = method_decorator(csrf_protect)
def meetup_details(request,slug):
    try:
        selected_meetups = Meetup.objects.get(slug=slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                participant, _ = Participants.objects.get_or_create(email=user_email)
                selected_meetups.participants.add(participant)
                return redirect("confirm",slug=slug)
        return render(request,"meetups/meetup-details.html",{
                "meetup":selected_meetups,
                "meetup_found":True,
                "form":registration_form
            })
    except:
        return(request,"meetups/meetup-details.html",{
            "meetup_found":False

        })

def confirm_registration(request,slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request,"meetups/registration-confirmation.html",{
        "meetup" : meetup
    })
from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="all-meetups"),
    path("<slug:slug>/registered",views.confirm_registration,name="confirm"),
    path("<slug:slug>",views.meetup_details,name="meetup-detail")
]
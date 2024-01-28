from django.contrib import admin
from .models import Meetup,Location,Participants
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("location","date")
    list_display=("title","date","location")

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participants)
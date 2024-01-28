from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{ self.name } ({self.address})"
    
class Participants(models.Model):
    email = models.EmailField(max_length=30,unique=True)
    
    def __str__(self):
        return self.email 
class Meetup(models.Model):
    title = models.CharField(max_length=50)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=200)
    image=models.ImageField(upload_to="images")
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants,blank=True,null=True)

    def __str__(self):
        return self.title

    

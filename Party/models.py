from django.db import models
# Create your models here.

class Party(models.Model):   
    #Unique Party identifier
    id = models.IntegerField(blank = False, null = False, primary_key = True)

    #Basic Details
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    hostedBy = models.ForeignKey('User.Organizer', related_name = 'hostedBy', on_delete = models.CASCADE, null = True, blank = True)
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)
    
    #Guest List
    # Need to add fields for attendance and payments 

    #Status
    status = models.CharField(max_length = 20, blank = False, default = "Upcoming",)

    class Meta:
        ordering = ('time',)

from django.db import models
# Create your models here.

class Party(models.Model):
    
    #Basic Details
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    hostedBy = models.ForeignKey('User.Organizer', related_name = 'parties', on_delete = models.CASCADE, null = False)
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)
    
    #Guest List
    attended = models.ManyToManyField('User.User', related_name = '%(class)s_attended')
    paidVenmo = models.ManyToManyField ('User.User', related_name = '%(class)s_paidVenmo')
    paidCash = models.ManyToManyField('User.User', related_name = '%(class)s_paidCash')

    #Status
    status = models.CharField(max_length = 20, blank = False, default = "Upcoming", on_delete = models.CASCADE)

    class Meta:
        ordering = ('time',)

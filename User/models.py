from django.db import models
# Create your models here.

class User(models.Model):
    #Unique Account Indentifier
    uniqueID = models.CharField(null = False, max_length = 30, unique = True)
    universityID = models.CharField(default = "ERROR: no UID", blank = False, max_length = 20)    

    #Basic Information
    firstName = models.CharField(null = False, max_length = 50)
    lastName = models.CharField(null = False, max_length = 50)
    college = models.CharField(default = "UCLA", max_length = 100)

    #Contact Information 
    email = models.CharField(null = False, max_length = 100)
    phone = models.CharField(default = "N/A", max_length = 20)

    #Account Type
    isOperator = models.BooleanField(default = False)
    isOrganizer = models.BooleanField(default = False)
    
    #Party-goer fields
    goingTo = models.ManyToManyField('Party.Party', related_name = '%(class)s_goingTo')
    attendedParties = models.ManyToManyField('Party.Party', related_name = '%(class)s_attenededParties')
    
class Operator(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Parties that the operator has checkIn priveleges for
    checkInPermissionsFor = models.ManyToManyField('Party.Party', related_name = '%(class)s_checkInPermissionsFor')
    
class Organizer(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Name of Organization that organizer hosts parties for
    organizationName = models.TextField(null = False)
    
    #Parties that are associated with this organizer
    #Check party field to see status of the party (Upcoming, Current, Past)
    parties = models.ForeignKey('Party.Party', on_delete=models.CASCADE)

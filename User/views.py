#-----------------------
# Purpose: all views associated with organizer's side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------
from User.models import User, Operator, Organizer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from User.serializers import UserSerializer, OperatorSerializer, OrganizerSerializer

#User API Views
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().filter(user=self.request.user)

#Operator API Views
class OperatorList(generics.ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OperatorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OperatorSerializer

    def get_queryset(self):
        return Operator.objects.all().filter(user=self.request.user)

#Organizer API View
class OrganizerList(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrganizerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizerSerializer

    def get_queryset(self):
        return Organizer.objects.all().filter(user=self.request.user)

#-----------------------
# Purpose: all views associated with organizer's side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------
from Party.models import Party
from rest_framework import generics
 
from Party.serializers import PartySerializer
 
 
class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
 
    def perform_create(self, serializer):
        serializer.save()
 
 
class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartySerializer
    lookup_field = 'partyid'
    def get_queryset(self):
        queryset = Party.objects.all()

        partyID = self.kwargs['partyid']
       
        if partyID is not None:
            queryset = queryset.filter(partyid = partyID)
            
        return queryset

class PartyManyDetail(generics.ListAPIView):
    serializer_class = PartySerializer
    lookup_field = 'partyid'
    
    def get_queryset(self):
        queryset = Party.objects.all()

        partyID = self.kwargs['partyid']

        if partyID is not None:
            queryset = queryset.filter(partyid__icontains = partyID)

        return queryset

class PartyCheckIn(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartySerializer
    lookup_field = 'partyid'
    def get_queryset(self):
        queryset = Party.objects.all()

        partyID = self.kwargs['partyid']

        if partyID is not None:
            queryset = queryset.filter(partyid = partyID)

        return queryset
        

from django.shortcuts import render
# generics are pre-bult views in DRF

from rest_framework import generics

from .serializers import BucketSerializer

from .models import BucketList

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    """ Defines the create behaviour of our rest api """
    queryset = BucketList.objects.all()
    serializer_class = BucketSerializer

    def perform_create(self, serializer):
        """ save the post when data creating a new bucketlist """
        serializer.save()

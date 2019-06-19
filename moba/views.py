from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from moba.serializers import HeroListSerializers
from moba.models import HeroList


# Create your views here.
class HeroListList(generics.ListCreateAPIView):
    queryset = HeroList.objects.all()
    serializer_class = HeroListSerializers
    name = 'hero-list'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'hero-list': reversed(HeroListList.name, request=request)})

from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from moba.serializers import HeroListSerializers, HeroSerializers, AbilitySerializers, DamgeCoolDownManaSerializer, \
    HeroItemSerializers
from moba.models import HeroList, Hero, AbilityItem, DamageCooldownMana, HeroItem
import logging
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from django_filters import rest_framework as filters


# Create your views here.
class HeroListList(generics.ListCreateAPIView):
    queryset = HeroList.objects.all()
    serializer_class = HeroListSerializers
    name = 'herolist'


class HeroListDetail(generics.ListCreateAPIView):
    serializer_class = HeroListSerializers
    name = 'herolist-detail'

    def get_queryset(self):
        username = self.kwargs['hero_id']
        print('Loggiing -->' + str(username))
        return HeroList.objects.filter(hero_id=username)


class HeroListView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers
    name = 'hero'


class HeroDetailView(generics.ListCreateAPIView):
    serializer_class = HeroSerializers
    name = 'hero-detail'

    def get_queryset(self):
        username = self.kwargs['hero_id']
        print('Loggiing -->' + str(username))
        return Hero.objects.filter(hero_id=username)


class AbilityListView(generics.ListCreateAPIView):
    queryset = AbilityItem.objects.all()
    serializer_class = AbilitySerializers
    name = 'ability'


class AbilityOfHeroView(generics.ListCreateAPIView):
    serializer_class = AbilitySerializers
    name = 'ability-hero'

    def get_queryset(self):
        username = self.kwargs['hero_id']
        print('Loggiing -->' + str(username))
        return AbilityItem.objects.filter(heroId=username)


class DamagaCooldownManaView(generics.ListCreateAPIView):
    queryset = DamageCooldownMana.objects.all()
    serializer_class = DamgeCoolDownManaSerializer
    name = 'dcm'


class DcmOfHeroView(generics.ListCreateAPIView):
    serializer_class = DamgeCoolDownManaSerializer
    name = 'dcm-hero'

    def get_queryset(self):
        username = self.kwargs['hero_id']
        print('Loggiing -->' + str(username))
        return DamageCooldownMana.objects.filter(heroId=username)


class HeroItemView(generics.ListCreateAPIView):
    queryset = HeroItem.objects.all()
    serializer_class = HeroItemSerializers
    name = 'hero-item'


class HeroItemListView(generics.ListCreateAPIView):
    queryset = HeroItem.objects.all()
    serializer_class = HeroItemSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id', 'itemid',)
    name = 'hero-item-detail'

    def get_queryset(self):
        id_list = self.kwargs['id'].split(' ')
        # id_list = [10, 12]
        if not id_list:
            return []
        return HeroItem.objects.filter(itemid__in=id_list)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'hero-list': reversed(HeroListList.name, request=request),
            'hero': reversed(HeroListView.name, request=request),
            'ability': reversed(AbilityListView.name, request=request),
            'dcm': reversed(DamagaCooldownManaView.name, request=request),
            'hero-item': reversed(HeroItemView.name, request=request),

        })

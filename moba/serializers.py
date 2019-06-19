from rest_framework import serializers
from moba.models import HeroList


class HeroListSerializers(serializers.HyperlinkedModelSerializer):
    # herolists = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='hero-list'
    # )
    class Meta:
        model = HeroList
        fields = (
            'hero_id',
            'name',
            'icon',
            'data_stars'
        )

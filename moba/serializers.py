from rest_framework import serializers
from moba.models import HeroList, Hero, AbilityItem, DamageCooldownMana, HeroItem


class HeroListSerializers(serializers.HyperlinkedModelSerializer):
    # heros = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name= 'hero-list'
    # )

    class Meta:
        model = HeroList
        fields = (
            'hero_id',
            'name',
            'icon',
            'data_stars'
        )


class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = (
            'hero_id',
            'icon',
            'name',
            'grey_name',
            'cost_in_gold',
            'voucher_code',
            'role',
            'specialty',
            'max_hp',
            'armor',
            'magic_defense',
            'attack_damage',
            'ability_power',
            'max_mana',
            'movement_speed',
            'magic_pierce',
            'attack_speed',
            'critical_chance',
            'critical_damage',
            'life_steal',
            'magic_life_steal',
            'cooldown_speed',
            'attack_range',
            'resistance',
            'hp_per_5_seconds',
            'mana_per_5_seconds',
            'max_energy',
            'regen_energy_per_5_seconds',
            'guide_youtube_link',
            'guide_text',
            'recommend_build'
        )


class AbilitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbilityItem
        fields = (
            'icon',
            'name',
            'heroId',
            'type',
            'description',
            'order'
        )


class DamgeCoolDownManaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DamageCooldownMana
        fields = (
            'order',
            'damage',
            'cooldown',
            'mana',
            'heroId',
            'table'
        )


class HeroItemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeroItem
        fields = (
            'image_urls',
            'fullname',
            'tier',
            'itemid',
            'info',
        )

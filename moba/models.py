from django.db import models


# Create your models here.
class HeroList(models.Model):
    hero_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=300)
    data_stars = models.CharField(max_length=100)

    class Meta:
        ordering = (('name'),)


class Hero(models.Model):
    hero_id = models.CharField(max_length=100)
    icon = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    grey_name = models.CharField(max_length=100)
    cost_in_gold = models.CharField(max_length=100)
    voucher_code = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    max_hp = models.CharField(max_length=100)
    armor = models.CharField(max_length=100, null=True)
    magic_defense = models.CharField(max_length=100, null=True)
    attack_damage = models.CharField(max_length=100, null=True)
    ability_power = models.CharField(max_length=100, null=True)
    max_mana = models.CharField(max_length=100, null=True)
    movement_speed = models.CharField(max_length=100, null=True)
    magic_pierce = models.CharField(max_length=100, null=True)
    attack_speed = models.CharField(max_length=100, null=True)
    critical_chance = models.CharField(max_length=100, null=True)
    critical_damage = models.CharField(max_length=100, null=True)
    life_steal = models.CharField(max_length=100, null=True)
    magic_life_steal = models.CharField(max_length=100, null=True)
    cooldown_speed = models.CharField(max_length=100, null=True)
    attack_range = models.CharField(max_length=100, null=True)
    resistance = models.CharField(max_length=100, null=True)
    hp_per_5_seconds = models.CharField(max_length=100, null=True)
    mana_per_5_seconds = models.CharField(max_length=100, null=True)
    max_energy = models.CharField(max_length=100, null=True)
    regen_energy_per_5_seconds = models.CharField(max_length=100, null=True)
    guide_youtube_link = models.CharField(max_length=100, null=True)
    guide_text = models.TextField()
    recommend_build = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = (('name'),)


class AbilityItem(models.Model):
    # define the fields for your item here like:
    icon = models.TextField()
    name = models.CharField(max_length=100)
    heroId = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    order = models.CharField(max_length=10, null=True)

    class Meta:
        ordering = (('name'),)


class DamageCooldownMana(models.Model):
    order = models.CharField(max_length=100)
    damage = models.CharField(max_length=100, null=True)
    cooldown = models.CharField(max_length=100, null=True)
    mana = models.CharField(max_length=100, null=True)
    heroId = models.CharField(max_length=100)
    table = models.CharField(max_length=100)

    class Meta:
        ordering = (('table'), ('order'),)


class HeroItem(models.Model):
    # other fields...
    image_urls = models.TextField()
    fullname = models.CharField(max_length=100)
    tier = models.CharField(max_length=200)
    itemid = models.IntegerField()
    info = models.TextField()

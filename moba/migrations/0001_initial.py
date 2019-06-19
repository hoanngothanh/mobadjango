# Generated by Django 2.2.1 on 2019-06-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=200)),
                ('data_stars', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
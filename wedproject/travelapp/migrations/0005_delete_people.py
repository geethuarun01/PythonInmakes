# Generated by Django 4.1.3 on 2022-12-12 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_rename_name_people_name1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='People',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-29 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]

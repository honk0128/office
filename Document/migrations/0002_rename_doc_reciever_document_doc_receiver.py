# Generated by Django 3.2.18 on 2023-05-22 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='Doc_Reciever',
            new_name='Doc_Receiver',
        ),
    ]

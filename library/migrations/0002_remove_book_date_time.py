# Generated by Django 3.1.3 on 2021-01-13 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_time',
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20210127_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='StudentID',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

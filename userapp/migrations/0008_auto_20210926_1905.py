# Generated by Django 3.2.6 on 2021-09-26 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_alter_needjob_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Needjob',
        ),
    ]

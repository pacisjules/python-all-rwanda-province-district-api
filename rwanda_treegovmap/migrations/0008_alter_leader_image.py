# Generated by Django 3.2.6 on 2021-09-30 07:55

from django.db import migrations, models
import rwanda_treegovmap.models


class Migration(migrations.Migration):

    dependencies = [
        ('rwanda_treegovmap', '0007_alter_leader_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='image',
            field=models.ImageField(blank=True, default='No-img.jpg', null=True, upload_to=rwanda_treegovmap.models.nameFile),
        ),
    ]

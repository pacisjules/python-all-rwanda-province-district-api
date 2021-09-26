# Generated by Django 3.2.6 on 2021-09-26 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rwanda_treegovmap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinces',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='occupation_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('PROVINCE', 'PROVINCE'), ('DISTRICT', 'DISTRICT'), ('SECTOR', 'SECTOR'), ('CELL', 'CELL')], max_length=255)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('reg_time', models.TimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+250788888888'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('leader_for', models.CharField(choices=[('PROVINCE', 'PROVINCE'), ('DISTRICT', 'DISTRICT'), ('SECTOR', 'SECTOR'), ('CELL', 'CELL')], max_length=255)),
                ('image', models.ImageField(default='Images/None/No-img.jpg', upload_to='ProfileImage/')),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('reg_time', models.TimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('occ_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rwanda_treegovmap.occupation_type')),
            ],
        ),
        migrations.AddField(
            model_name='provinces',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rwanda_treegovmap.leader'),
        ),
    ]
from django.db import models
from userapp.models import User
from django.core.validators import RegexValidator

# Create your models here.

#0. OCCUPATION MODEL
class occupation_type(models.Model):
    type_levels = [
        ('PROVINCE', 'PROVINCE'),
        ('DISTRICT', 'DISTRICT'),
        ('SECTOR', 'SECTOR'),
        ('CELL', 'CELL'),
    ]
    type_name=models.CharField(max_length=255, unique=True)
    type=models.CharField(max_length=255, choices=type_levels)
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.type_name

#1. LEADER MODEL

def nameFile(instance, filename):
    return '/'.join(['ProfileImage', str(instance.names), filename])


class leader(models.Model):
    reader_for = [
        ('PROVINCE', 'PROVINCE'),
        ('DISTRICT', 'DISTRICT'),
        ('SECTOR', 'SECTOR'),
        ('CELL', 'CELL'),
    ]
    names=models.CharField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+250788888888'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    leader_for=models.CharField(max_length=255, choices=reader_for)
    occ_type=models.ForeignKey(occupation_type, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=nameFile, default='No-img.jpg', blank=True, null=True)
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.names

 #2. PROVINCE MODEL
class provinces(models.Model):
    name=models.CharField(max_length=255, unique=True)
    leader=models.ForeignKey(leader, on_delete=models.CASCADE, null=True)
    surface=models.FloatField(max_length=255)
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

#3. DISTRICT MODEL
class district(models.Model):
    name=models.CharField(max_length=255, unique=True)
    leader=models.ForeignKey(leader, on_delete=models.CASCADE, null=True)
    province=models.ForeignKey(provinces, on_delete=models.CASCADE, null=True)
    popularity=models.IntegerField()
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


#4. SECTOR MODEL
class sector(models.Model):
    name=models.CharField(max_length=255, unique=True)
    leader=models.ForeignKey(leader, on_delete=models.CASCADE, null=True)
    province=models.ForeignKey(provinces, on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


#5. CELL MODEL
class cell(models.Model):
    name=models.CharField(max_length=255, unique=True)
    leader=models.ForeignKey(leader, on_delete=models.CASCADE, null=True)
    province=models.ForeignKey(provinces, on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    sector=models.ForeignKey(sector, on_delete=models.CASCADE, null=True)
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


#6. DISTRICT GALLERY MODEL
class district_gallery(models.Model):
    name=models.CharField(max_length=255)
    province=models.ForeignKey(provinces, on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='GalleryImages/')
    reg_date=models.DateField(auto_now_add=True)
    reg_time=models.TimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name 



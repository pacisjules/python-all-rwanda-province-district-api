from django.contrib import admin
from .models import provinces,leader,occupation_type,district,sector,cell,district_gallery

admin.site.register(provinces)
admin.site.register(leader)
admin.site.register(occupation_type)
admin.site.register(district)
admin.site.register(sector)
admin.site.register(cell)
admin.site.register(district_gallery)


# Register your models here.

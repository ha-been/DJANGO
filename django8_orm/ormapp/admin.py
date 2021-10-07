from django.contrib import admin
from ormapp.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    
admin.site.register(Profile, ProfileAdmin)
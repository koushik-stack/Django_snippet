from django.contrib import admin

# Register your models here.
from user.models.author_model import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

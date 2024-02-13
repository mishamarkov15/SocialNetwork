from django.contrib import admin

from home import models


@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "first_name", "last_name")
    list_display_links = ("pk", "email")

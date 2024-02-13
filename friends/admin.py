from django.contrib import admin

from friends import models


@admin.register(models.Friends)
class FriendAdmin(admin.ModelAdmin):
    pass

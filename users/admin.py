from django.contrib import admin

from users.models import User

# admin.site.register(Category)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', )

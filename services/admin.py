from django.contrib import admin

from services.models import Sale, Making

# admin.site.register(Category)

@admin.register(Sale)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('material', 'weight')

@admin.register(Making)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('material', 'weight')
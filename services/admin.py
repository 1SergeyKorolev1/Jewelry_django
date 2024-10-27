from django.contrib import admin

from services.models import Sale

# admin.site.register(Category)

@admin.register(Sale)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('material', 'weight')
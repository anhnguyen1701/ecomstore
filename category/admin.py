from django.contrib import admin

from category.models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} # suggest slug by categoryname
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
from django.contrib import admin

from blogsApp.models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("category",)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)


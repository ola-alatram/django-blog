from django.contrib import admin

from blogsApp.models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)


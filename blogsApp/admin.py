from django.contrib import admin

from blogsApp.models import Blog, Category, ContactMessage

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("category",)}


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "date",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = ("-date",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)


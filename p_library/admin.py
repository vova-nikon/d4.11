from django.contrib import admin
from p_library.models import Book, Author, Publisher

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name')
    fields = ('ISBN', 'title', 'publisher', 'description', 'year_release', 'author', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
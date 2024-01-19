from django.contrib import admin
from .models import BooksModel,BookAuthorModel,AuthorModel,ReviewBookModel
# Register your models here.

class InlineModel(admin.TabularInline):
    model = BookAuthorModel

class BooksModelAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_price','isbn','create_at')
    list_filter = ('book_name','create_at')
    search_fields = ('book_name','isbn')
    ordering = ('book_name',)
    inlines = [InlineModel]




admin.site.register(BooksModel,BooksModelAdmin)
admin.site.register(BookAuthorModel)
admin.site.register(AuthorModel)
admin.site.register(ReviewBookModel)

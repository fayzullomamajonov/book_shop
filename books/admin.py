from django.contrib import admin
from .models import BooksModel,BookAuthorModel,AuthorModel,ReviewBookModel
# Register your models here.


admin.site.register(BooksModel)
admin.site.register(BookAuthorModel)
admin.site.register(AuthorModel)
admin.site.register(ReviewBookModel)

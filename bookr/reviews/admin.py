from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
                            BookContributor, Review)


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    search_help_text = 'enter title or isbn'
    search_fields = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')

    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4],
                                       obj.isbn[4:6], obj.isbn[6:11],
                                       obj.isbn[11:13])


class ContributorAdmin(admin.ModelAdmin):
    list_filter = ('last_names',)
    list_display = ('first_names', 'last_names')
    search_fields = ('last_names',)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)

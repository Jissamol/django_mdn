from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register Genre and Language
admin.site.register(Genre)
admin.site.register(Language)

class BooksInstanceInline(admin.TabularInline):
    """Inline editing for BookInstance within the Book model."""
    model = BookInstance
    extra = 0  # Prevents adding empty extra forms by default

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin configuration for Book model."""
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'genre')

    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        """Display genres as a comma-separated list."""
        return ", ".join(genre.name for genre in obj.genre.all())
    display_genre.short_description = 'Genre'

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Admin configuration for BookInstance model."""
    list_display = ('book', 'status', 'due_back', 'borrower', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id', 'borrower')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

    list_select_related = ('book', 'borrower')  # Optimizes query performance

@admin.register(Author)  
class AuthorAdmin(admin.ModelAdmin):
    """Admin configuration for Author model."""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

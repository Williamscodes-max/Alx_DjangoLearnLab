from django.db import models

# =========================
# Author Model
# =========================
class Author(models.Model):
    """
    Model to store author information.
    
    Fields:
    - name: Stores the full name of the author (string, max 100 characters)
    
    Relationships:
    - Has many Books (one-to-many)
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        # Returns the author's name when object is printed
        return self.name


# =========================
# Book Model
# =========================
class Book(models.Model):
    """
    Model to store information about books.
    
    Fields:
    - title: Title of the book (string, max 200 characters)
    - publication_year: Year the book was published (integer)
    - author: Foreign key linking to the Author model (one author can have many books)
    
    Relationships:
    - Each book belongs to one author (many-to-one)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        related_name='books',  # allows author.books.all() to get all books by this author
        on_delete=models.CASCADE  # deletes book if the related author is deleted
    )

    def __str__(self):
        # Returns the book's title when object is printed
        return self.title

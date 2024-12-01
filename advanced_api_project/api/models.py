from django.db import models

class Author(models.Model):
    # The Author model stores information about authors
    name = models.CharField(max_length=100)  # Field to store author's name

    def __str__(self):
        return self.name


class Book(models.Model):
    # The Book model stores information about books and links them to authors
    title = models.CharField(max_length=200)  # Field to store book's title
    publication_year = models.IntegerField()  # Field to store the publication year
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # ForeignKey to Author

    def __str__(self):
        return self.title
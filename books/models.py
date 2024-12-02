from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    birth_year = models.IntegerField(verbose_name="Birth year", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")  
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    year = models.IntegerField(verbose_name="Year", null=True, blank=True) 
    pages = models.IntegerField(verbose_name="Pages", null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(verbose_name="publishing date")
    epub = models.FileField(upload_to='books/epubs/')
    cover = models.ImageField(upload_to='books/covers/')

    def __str__(self):
        return self.title

    # override predefined model method to delete files stored in the system
    def delete(self, *args, **kwargs):
        self.epub.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

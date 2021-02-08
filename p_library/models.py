from django.db import models

# Create your models here.

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=999, decimal_places=2, default=1)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    friend = models.ForeignKey('Friend', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title


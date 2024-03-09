from django.db import models
from django.urls import reverse
# Create your models here.

class Bigges(models.Model):
    img = models.ImageField(upload_to='big/')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='big/')

    def __str__(self):
        return self.name

class Small(models.Model):
    image = models.ImageField(upload_to='small/')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    status = models.TextField()
    def get_absolute_url(self):
        return reverse('smallDetail', args=[self.slug])
    def __str__(self):
        return self.name

class Manfor(models.Model):
    status = models.TextField()
    image = models.ImageField(upload_to='manfor/')

    def __str__(self):
        return self.status



class Womanfor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='manfor')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse('womanforDetail', args=[self.slug])

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    numbers = models.IntegerField()
    massage = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Watch(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='watch/')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300)

    def get_absolute_url(self):
        return reverse('watchDetail', args=[self.slug])
    def __str__(self):
        return self.name

class Komputer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='komputer/')
    bio = models.TextField()
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300)
    def get_absolute_url(self):
        return reverse('komputerDetail', args=[self.slug])

    def __str__(self):
        return self.name

class Koylak(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    img = models.ImageField(upload_to='koylak/')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=220)
    def get_absolute_url(self):
        return reverse('koylakDetail', args=[self.slug])

    def __str__(self):
        return self.name
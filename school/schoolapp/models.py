from django.db import models


# Create your models here.
class Banner(models.Model): 
    name = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to='images/')



class Notice(models.Model):
    title = models.CharField(max_length=50)
    description =models.CharField(max_length=150)
    attach_file = models.FileField(upload_to='notice/')



class Gallery(models.Model):
    title_g=models.CharField(max_length=50)
    images_g=models.FileField(upload_to='images/')

class Teachernot(models.Model):
    title = models.CharField(max_length=50)
    description =models.CharField(max_length=150)
    attach_file = models.FileField(upload_to='notice/')

class Teacher_data(models.Model):
    name = models.CharField(max_length=50)
    deg =models.CharField(max_length=150)
    img = models.FileField(upload_to='images/')
    join_date = models.CharField(max_length=20)

class Events_mod(models.Model):
    events_name = models.CharField(max_length=50)
    events_link = models.CharField(max_length=50)
    class Meta:
        db_table="Events"


class Rok_head(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
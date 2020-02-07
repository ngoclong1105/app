from django.db import models

from django.contrib.auth.models import AbstractUser
import os
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()
IMG_DIR = os.path.join('asset', 'comic_images')
IMG_URL_PREFIX = '/asset/comic_images/'


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20)

class Media1(models.Model):
    src = models.TextField()

class Inf1(models.Model):
    src= models.TextField()
class Inf2(models.Model):
    src= models.TextField()
class Spiderman(models.Model):
    src = models.TextField()
class Doctor(models.Model):
    src = models.TextField()
class Hulk(models.Model):
    src = models.TextField()
class Ironman(models.Model):
    src = models.TextField()
class Thor(models.Model):
    src = models.TextField()
class Daredevil(models.Model):
    src = models.TextField()
class Comment(models.Model):
    reply = models.TextField(max_length=50,db_column='comment')
    name = models.TextField(default="")

class Comic(models.Model):
    code = models.CharField(max_length=20, verbose_name='Mã truyện', unique=True)
    name = models.CharField(max_length=50, verbose_name='Tên truyện')
    description = models.CharField(blank=True, verbose_name='Mô tả', max_length=200)
    unitPrice = models.FloatField(db_column='unit_price', verbose_name='Đơn giá')
    imageURL = models.CharField(db_column='image_url', max_length=1024, default="")
        
    def saveImage(self, image):
        imgPath = os.path.join(IMG_DIR, image.name)
        savedPath = fs.save(imgPath, image)
        fileName = os.path.basename(savedPath)

        self.imageURL = IMG_URL_PREFIX + fileName
        self.save()

    def delete(self):
        fileName = self.imageURL.split('/')[-1]
        imgPath = os.path.join(IMG_DIR, fileName)
        
        if os.path.isfile(imgPath):
            os.remove(imgPath)

        super().delete()


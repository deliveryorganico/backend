from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Profile(AbstractUser):
    ''' Foreign Keys '''
    address = models.ForeignKey('Address')
    favorite = models.ForeignKey('Favorite')

    ''' Atributes '''
    is_company = models.BooleanField(default=False)
    photo = models.ImageField(null=True)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.username)


class Address(models.Model):
    ''' Foreign Keys '''
    city = models.ForeignKey('City')
    locality = models.ForeignKey('Locality')

    ''' Atributes '''
    address = models.CharField(max_length=60)
    alias = models.CharField(max_length=40)
    floor = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(-50)], null=True)
    phone = models.CharField(max_length=30)
    st_number = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(10000)])
    zip_code = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(10000)])

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.alias)

class City(models.Model):
    ''' Foreign Keys '''
    locality = models.ForeignKey('Locality')

    ''' Atributes '''
    CITIES=(
        ('CBA', 'Cordoba'),
        ('MDZ', 'Mendoza'),
    )
    city = models.CharField(max_length=3, choices=CITIES)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.city)

class Locality(models.Model):
    ''' Atributes '''
    LOCALITIES=(
        ('CBA', 'Cordoba'),
        ('MDZ', 'Mendoza'),
    )
    locality = models.CharField(max_length=3, choices=LOCALITIES)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.locality)

class Company(models.Model):
    ''' Foreign Keys '''
    address=models.ForeignKey('Address')
    branch=models.ForeignKey('Branch')

    '''Atributes'''
    name=models.CharField(max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    '''Foreign Keys'''
    address=models.ForeignKey('Address')
    product=models.ForeignKey('Product')

    '''Atributes'''
    reputation=models.FloatField(validators=[MaxValueValidator(0.0), MinValueValidator(5.0)])
    n_phone=models.CharField(max_length=30)
    name=models.CharField(max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}, {}'.format(self.name, self.reputation)
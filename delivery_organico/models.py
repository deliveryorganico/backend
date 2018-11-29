from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class City(models.Model):
    ''' Foreign Keys '''

    ''' Atributes '''
    city = models.CharField('Ciudad',max_length=15)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.city)

class Locality(models.Model):
    ''' Foreign Keys '''

    ''' Atributes '''
    locality = models.CharField('Localidad',max_length=15)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.locality)

class Profile(AbstractUser):
    ''' Foreign Keys '''

    ''' Atributes '''
    is_company = models.BooleanField('Compania', default=False)
    photo = models.ImageField('Foto',null=True)
    city = models.CharField('Ciudad', max_length=15)
    locality = models.CharField('Localidad', max_length=15)
    address = models.CharField('Direccion',max_length=60)
    floor = models.IntegerField('Piso',validators=[MaxValueValidator(100), MinValueValidator(-50)], default=0)
    phone = models.CharField('Telefono',max_length=30)
    st_number = models.IntegerField('Altura',validators=[MaxValueValidator(10000), MinValueValidator(0)],default=0)
    zip_code = models.IntegerField('Zip',validators=[MaxValueValidator(10000), MinValueValidator(0)], default=0)

    ''' Functions '''


class Address(models.Model):
    ''' Foreign Keys '''
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='fk_cityAddress')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='fk_localityAddress')

    ''' Atributes '''
    address = models.CharField('Direccion',max_length=60)
    alias = models.CharField('Alias',max_length=40)
    floor = models.IntegerField('Piso',validators=[MaxValueValidator(100), MinValueValidator(-50)],default=0)
    phone = models.CharField('Telefono',max_length=30)
    st_number = models.IntegerField('Altura',validators=[MaxValueValidator(10000), MinValueValidator(0)])
    zip_code = models.IntegerField('Zip',validators=[MaxValueValidator(10000), MinValueValidator(0)])

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.alias)

class Company(models.Model):
    ''' Foreign Keys '''
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='fk_addressCompany')

    '''Atributes'''
    name = models.CharField('Nombre',max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    '''Foreign Keys'''
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='fk_addressBranch')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='fk_companyBranch')

    '''Atributes'''
    reputation = models.FloatField('Reputuacion',validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    n_phone = models.CharField('Telefono',max_length=30)
    name = models.CharField('Nombre',max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}, {}'.format(self.name, self.reputation)

class Product(models.Model):
    '''Foreign Keys'''
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='fk_branchProduct')

    ''' Atributes '''
    title = models.CharField('Title',max_length=30)
    description = models.CharField('Descripcion',max_length=70)
    price = models.FloatField('Precio',validators=[MaxValueValidator(500000.0), MinValueValidator(0.0)])

    ''' Functions '''

    def __str__(self):
        return '{}, {}'.format(self.title, self.price)

class Favorite(models.Model):
    ''' Foreign Keys '''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='fk_profileFavorite')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='fk_branchFavorite')

    '''Functions'''
    def __str__(self):
        return '{},{}'.format(self.profile, self.branch)

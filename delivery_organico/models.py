from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class City(models.Model):
    ''' Foreign Keys '''

    ''' Atributes '''
    CITIES = (
        ('CBA', 'Cordoba'),
        ('MDZ', 'Mendoza'),
    )
    city = models.CharField(max_length=3, choices=CITIES)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.city)

class Locality(models.Model):
    ''' Foreign Keys '''

    ''' Atributes '''
    LOCALITIES = (
        ('CBA', 'Cordoba'),
        ('MDZ', 'Mendoza'),
    )
    locality = models.CharField(max_length=3, choices=LOCALITIES)

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.locality)

class Profile(AbstractUser):
    ''' Foreign Keys '''

    ''' Atributes '''
    is_company = models.BooleanField(default=False)
    photo = models.ImageField(null=True)

    ''' Functions '''
    def set_vcards(self, vcards):
        """
        Expects a list of vcards like [{'type_of_card':'xxx', 'data':'xxx'},]
        Deletes previous vcards, and sets the new ones.
        """
        self.vcards.all().delete()
        for vcard in vcards:
            new_vcard = VCard()
            new_vcard.type_of_card = vcard['type_of_card']
            new_vcard.data = vcard['data']
            new_vcard.user = self
            new_vcard.save()


    def __str__(self):
        return '{}'.format(self.username)

class VCard(models.Model):
    '''
    Generic contact card.
    '''
    PHONE = 'phone'
    EMAIL = 'email'
    ADDRESS = 'address'
    LINK = 'link'
    TYPES_AVAILABLES=(
        (EMAIL,'Email'),
        (PHONE,'Teléfono'),
        (ADDRESS,'Dirección'),
        (LINK, 'Link'),
    )

    type_of_card = models.CharField("Tipo de dato",
        choices=TYPES_AVAILABLES,
        max_length=20)
    data = models.CharField("Valor", max_length=128)
    upload_date = models.DateTimeField('Last change', auto_now=True)
    user = models.ForeignKey(Profile, related_name='vcards', null=True, blank=True, on_delete=models.CASCADE)


class Address(models.Model):
    ''' Foreign Keys '''
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='fk_cityAddress')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='fk_localityAddress')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='fk_profileAddress')

    ''' Atributes '''
    address = models.CharField(max_length=60)
    alias = models.CharField(max_length=40)
    floor = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(-50)], null=True)
    phone = models.CharField(max_length=30)
    st_number = models.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(0)])
    zip_code = models.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(0)])

    ''' Functions '''
    def __str__(self):
        return '{}'.format(self.alias)

class Company(models.Model):
    ''' Foreign Keys '''
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='fk_addressCompany')

    '''Atributes'''
    name = models.CharField(max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    '''Foreign Keys'''
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='fk_addressBranch')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='fk_companyBranch')

    '''Atributes'''
    reputation = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    n_phone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    '''Functions'''
    def __str__(self):
        return '{}, {}'.format(self.name, self.reputation)

class Product(models.Model):
    '''Foreign Keys'''
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='fk_branchProduct')

    ''' Atributes '''
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=70)
    price = models.FloatField(validators=[MaxValueValidator(500000.0), MinValueValidator(0.0)])

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

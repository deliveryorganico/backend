# Generated by Django 2.1.2 on 2018-10-19 16:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_company', models.BooleanField(default=False, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=40)),
                ('floor', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(-50)])),
                ('phone', models.CharField(max_length=30)),
                ('st_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('zip_code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reputation', models.FloatField(validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)])),
                ('n_phone', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_addressBranch', to='delivery_organico.Address')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('CBA', 'Cordoba'), ('MDZ', 'Mendoza')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_addressCompany', to='delivery_organico.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_branchFavorite', to='delivery_organico.Branch')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_profileFavorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(choices=[('CBA', 'Cordoba'), ('MDZ', 'Mendoza')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=70)),
                ('price', models.FloatField(validators=[django.core.validators.MaxValueValidator(500000.0), django.core.validators.MinValueValidator(0.0)])),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_branchProduct', to='delivery_organico.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_companyBranch', to='delivery_organico.Company'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_cityAddress', to='delivery_organico.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_localityAddress', to='delivery_organico.Locality'),
        ),
    ]

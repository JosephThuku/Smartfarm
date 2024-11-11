# Generated by Django 5.1.2 on 2024-11-09 14:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('optimal_temperature', models.FloatField()),
                ('optimal_humidity', models.FloatField()),
                ('optimal_soil_moisture', models.FloatField()),
                ('growing_season', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('soil_type', models.CharField(max_length=50)),
                ('total_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('soil_moisture', models.FloatField()),
                ('rainfall', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environmental_data', to='farm.farm')),
            ],
            options={
                'verbose_name_plural': 'Environmental Data',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('phone_number', models.CharField(help_text='Contact phone number', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('farm_size', models.DecimalField(blank=True, decimal_places=2, help_text='Farm size in acres', max_digits=10, null=True)),
                ('preferred_language', models.CharField(choices=[('en', 'English'), ('sw', 'Swahili')], default='en', max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='farmer_set', related_query_name='farmer', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='farmer_set', related_query_name='farmer', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Farmer',
                'verbose_name_plural': 'Farmers',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='farm.farmer'),
        ),
        migrations.CreateModel(
            name='FarmCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planting_date', models.DateField()),
                ('expected_harvest_date', models.DateField()),
                ('area_planted', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('planted', 'Planted'), ('growing', 'Growing'), ('harvested', 'Harvested')], default='planning', max_length=20)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.crop')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_crops', to='farm.farm')),
            ],
            options={
                'unique_together': {('farm', 'crop', 'planting_date')},
            },
        ),
    ]
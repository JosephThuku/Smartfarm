from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Farmer(AbstractUser):
    """
    Custom user model for farmers with additional fields for contact information
    """
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=False,
        help_text="Contact phone number"
    )
    
    # Email is already included in AbstractUser, but we'll make it required
    email = models.EmailField(_('email address'), unique=True)
    
    # Additional farmer-specific fields
    farm_size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Farm size in acres",
        null=True,
        blank=True
    )
    
    preferred_language = models.CharField(
        max_length=10,
        choices=[('en', 'English'), ('sw', 'Swahili')],
        default='en'
    )
    
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'

    def __str__(self):
        return f"{self.get_full_name()} ({self.phone_number})"

class Crop(models.Model):
    """
    Model to store crop information and optimal growing conditions
    """
    name = models.CharField(max_length=100)
    optimal_temperature = models.FloatField()
    optimal_humidity = models.FloatField()
    optimal_soil_moisture = models.FloatField()
    growing_season = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Farm(models.Model):
    """
    Model to store farm information
    """
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    soil_type = models.CharField(max_length=50)
    total_area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.farmer.get_full_name()}"

class FarmCrop(models.Model):
    """
    Model to track crops planted in each farm
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_crops')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    planting_date = models.DateField()
    expected_harvest_date = models.DateField()
    area_planted = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planning'),
            ('planted', 'Planted'),
            ('growing', 'Growing'),
            ('harvested', 'Harvested')
        ],
        default='planning'
    )
    
    class Meta:
        unique_together = ['farm', 'crop', 'planting_date']

class EnvironmentalData(models.Model):
    """
    Model to store environmental sensor data
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='environmental_data')
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    rainfall = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Environmental Data'

    def __str__(self):
        return f"{self.farm.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
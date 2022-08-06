from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from picklefield import PickledObjectField

from .managers import CustomUserManager

# Create your models here.

# class AuthRecord(models.Model):
#     # These two fields define a unique AuthRecord: the name of the
#     # provider and the identifier the provider uses to identify the
#     # user, which if possible should be stable across changes in
#     # screen names.
#     provider = models.CharField(max_length=32, db_index=True)
#     uid = models.CharField(max_length=128)

#     # The Django User associated with the provider-uid pair.
#     user = models.ForeignKey(User, related_name="singlesignon", db_index=True, on_delete=models.CASCADE)

#     # Profile information returned by the most recent OAuth callback, etc.
#     auth_token = PickledObjectField()
#     profile = PickledObjectField()

#     # General metadata.
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Authentication Record"
#         unique_together = (("provider", "uid"),)

#     # don't add any ordering because it causes mysql filesort on joins

    # def __unicode__(self):
    #     return self.provider + " " + self.uid[0:10] + " -> " + self.user.username

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Creates a user using the defined manager"""
    
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=50, blank=False, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Users' types
    is_idea_owner = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
 

class IdeaOwner(models.Model):
    
    # Define gender
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    # Define marital status
    SINGLE = 'S'
    MARRIED = 'M'
    DIVORCED = 'D'
    
    MARITAL_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
    ]

    # Idea owner details (DB fields)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    username = models.CharField(max_length=255, verbose_name='Username')
    occupation = models.CharField(max_length=255)
    gender = models.CharField(max_length=60,
                choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=60,
                choices=MARITAL_CHOICES)
    # NIN
    id_number = models.CharField(max_length=250)
    bio = models.TextField()
    
    # Company details
    cac_number = models.BigIntegerField() # Change this
    
    def __str__(self):
        return self.user.username


class Idea(models.Model):
    
    # Define the business category
    TECHNOLOGY = 'TE'
    AGRICULTURE = 'AG'
    EDUCATION = 'ED'
    MANUFACTURING = 'MN'
    
    CATEGORY_CHOICES = [
        (AGRICULTURE, 'Agriculture'),
        (TECHNOLOGY, 'Technology'),
        (EDUCATION, 'Education'),
        (MANUFACTURING,'Manufacturing'),
    ]
    # Define the stages
    IDEATION = 'ID'
    STARTUP = 'ST'
    GROWTH = 'GR'
    MATURE = 'MT'
    
    STAGE_CHOICES = [
        (IDEATION, 'Ideation Stage'),
        (STARTUP, 'Startup stage'),
        (GROWTH, 'Growth stage'),
        (MATURE, 'Matured stage'),
    ]
    # DB fields
    title = models.CharField(max_length=250)
    categories = models.CharField(max_length=15,
            choices=CATEGORY_CHOICES,
            default=TECHNOLOGY)
    stages = models.CharField(max_length=25, 
            choices=STAGE_CHOICES,
            default = IDEATION)
    
    # Idea details
    idea_details = models.TextField()
    idea_pitch = models.FileField(upload_to='uploads/')
    completion_timeline = models.DateField()
    estimated_cost = models.BigIntegerField() # Change this
    user = models.ForeignKey(IdeaOwner, related_name='ideas', on_delete=models.CASCADE)

    
class Investor(models.Model):
    # Define gender
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    username = models.CharField(max_length=255, verbose_name='Username')
    gender = models.CharField(max_length=60,
                choices=GENDER_CHOICES)
    # NIN
    id_number = models.CharField(max_length=250)
    bio = models.TextField()
    source_of_income = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username
    
class Company(models.Model):
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images') # company's logo
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=255, verbose_name='First Name')
    sector = models.CharField(max_length=250)
    
    # Company/Idea details
    cac_number = models.BigIntegerField()
    
    def __str__(self):
        return self.user.username
    

    
    
from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    
    GENDERS = (
        ('m', 'Man'),
        ('f', 'Woman')
    )
    
    username = models.CharField(
        error_messages={'unique': 'A user with that nick already exists.'}, 
        help_text='Required. 25 characters or fewer. Letters, digits and @/./+/-/_ only.', 
        max_length=25, 
        unique=True,  
        verbose_name='Nickname',
        blank=True, 
        )
    gender = models.CharField('Gender', max_length=1, choices=GENDERS, default='m')
    birth_date = models.DateField('Date of Birth', default='2000-09-12')


    def __str__(self):
        return self.username
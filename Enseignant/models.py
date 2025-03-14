from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def verif_username(value):
    if len(value)>10:
        raise ValidationError("Le nom d'utilisateur doit être inférieur à 10 caractères !")
    

class Enseignant(AbstractUser):
    username = models.CharField(max_length=20,unique=True,validators=[verif_username])
    
    
    class Meta : 
        verbose_name = "Enseignant"
        
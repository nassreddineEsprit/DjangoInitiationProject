from django.db import models
from Enseignant.models import Enseignant
from django.core.exceptions import ValidationError
from django.utils import timezone

cat_list = (("Web","Web"),("Mobile","Mobile"),("Bi ","Bi"))
# Create your models here.
def verif_date_pub(value):
    if value < timezone.now():
        raise ValidationError("La date de publication doit être supérieur à la date actuelle")


class Cours(models.Model):
    code = models.CharField(max_length=20,primary_key=True)
    titre = models.CharField(max_length=20)
    categorie = models.CharField(max_length=20,choices=cat_list)   
    date_publication=models.DateTimeField(validators=[verif_date_pub])
    tuteur = models.ForeignKey(Enseignant,on_delete = models.SET_NULL,null=True,related_name="cours")

    def __str__(self):
        return self.titre + " " + self.categorie + " " + self.date_publication.strftime("%d/%m/%Y") + " " + self.tuteur.username
    
    class Meta :
        verbose_name = "Cours"
from django.forms import *
from .models import Cours



class CoursForm(ModelForm):
    class Meta : 
        model = Cours 
        fields = "__all__"
        exclude = ("tuteur",)
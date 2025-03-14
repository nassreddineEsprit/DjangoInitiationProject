from django.urls import path
from .views import list_cours,UpdateCours,DeleteCours,CreateCours


urlpatterns = [
    path('list_cours/', list_cours, name="list_cours"),
    path('update/<str:pk>', UpdateCours.as_view(), name="update"),
    path('delete/<int:code>/', DeleteCours, name="delete"),
    path('add/', CreateCours.as_view(), name="add")


]
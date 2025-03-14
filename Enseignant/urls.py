from django.urls import path

from .views import listEnseignantWithCours,signin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('listEnseignant/', listEnseignantWithCours, name="listenseignant"),
    path('login/', signin, name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

]
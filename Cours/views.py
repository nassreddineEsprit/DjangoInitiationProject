from django.shortcuts import render,redirect
from django.views.generic import UpdateView,CreateView
from .forms import CoursForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cours


# Create your views here.
def list_cours(request):
    cours = Cours.objects.all()  
    return render(request, "list_cours.html", {"cours": cours})

class UpdateCours (UpdateView):
    model = Cours
    form_class = CoursForm
    template_name = "updatecours.html"
    success_url = reverse_lazy("list_cours")

def DeleteCours(request, code):
    cours = Cours.objects.get(code=code)
    if cours:
        cours.delete()
    return redirect("list_cours")

class CreateCours(LoginRequiredMixin,CreateView):
    model = Cours
    form_class = CoursForm
    template_name = "createcours.html"
    success_url = reverse_lazy("list_cours")
    def form_valid(self,form):
      form.instance.tuteur = self.request.user
      return super().form_valid(form)
    
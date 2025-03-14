from django.contrib import admin
from .models import Cours

# Register your models here.
def web (ModelAdmin, request, queryset):
    queryset.update(categorie="Web")

def mobile (ModelAdmin, request, queryset):
    queryset.update(categorie="Mobile")

def bi (ModelAdmin, request, queryset):
    queryset.update(categorie="BI")

web.short_description = "Changer la catégorie en web"
mobile.short_description = "Changer la catégorie en mobile"
bi.short_description = "Changer la catégorie en Bi"


@admin.register(Cours)
class CoursAdmin (admin.ModelAdmin):
    list_display = ("titre","categorie","date_publication","tuteur",)
    search_fields = ("titre","categorie",)
    list_filter = ("categorie",)
    actions = [web,mobile,bi]

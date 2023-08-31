from django.contrib import admin
from AppCoder import models
from .models import Libro, Comentario


# Register your models here.

admin.site.register(models.Libro)
admin.site.register(Comentario)
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.core.validators import FileExtensionValidator
from django.urls import reverse

# Create your models here.
    
TYPE_CHOICES = (
    ('Literatura', 'Literatura'),
    ('Matemática', 'Matemática'),
    ('Comunicación','Comunicación y Lenguaje'),
    ('Historia','Historia'),
    ('Varios','Libros varios'),
)

class Libro(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    autor = models.CharField(max_length=100, blank=False)
    pais = models.CharField(max_length=50, blank=True)
    año = models.IntegerField()
    editorial = models.CharField(max_length=100, blank=True)
    edicion = models.CharField(max_length=100, blank=True)
    resumen = models.TextField(default="Resumen...", max_length=500)
    tema = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=False)
    link = models.CharField(max_length=200, blank=False)

    




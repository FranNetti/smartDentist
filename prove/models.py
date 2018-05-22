"""
Definition of models.
"""

from django.db import models
from djangotoolbox.fields import EmbeddedModelField

class Dispositivo(models.Model):
    codDispositivo = models.IntegerField()
    login = models.DateTimeField(auto_now_add=True)
    dottore = EmbeddedModelField('Dottore')
    posizione = EmbeddedModelField('Posizione')

class Dottore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateTimeField(auto_now_add=True)

class Posizione(models.Model):
    lat = models.DecimalField(max_digits=3, decimal_places=2)
    long = models.DecimalField(max_digits=3, decimal_places=2)

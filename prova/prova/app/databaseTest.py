#import pymongo
#from pymongo import MongoClient

#class DBConnection(object):
    
#    def __init__(self, host="localhost", port=27017, db="database"):
#        super().__init__()    
#        self.conn = MongoClient(host, port)[db]

#    def find(self, field, value):
#        elem = self.conn.dispositivi.find({ field : value })
#        for p in elem:
#            return p["login"]
        

from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

class Forno(models.Model):
    codDispositivo = models.IntegerField()
    login = models.DateTimeField(auto_now_add=True)
    dottore = EmbeddedModelField('Dottore')
    posizione = EmbeddedModelField('Posizione')

class Dottore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateTimeField(auto_now_add=True)

class Posizione(models.Model):
    lat = models.DecimalField()
    long = models.DecimalField()
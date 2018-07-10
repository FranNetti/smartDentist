from django.db import models

# Class that identifies the table Doctor inside the database
class Doctor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthDate = models.DateTimeField()

    def __str__(self):
        return "Dr. {} {}".format(self.name,self.surname)

# Class that identifies the table Device inside the database
class Device(models.Model):
    device_id = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    lat = models.DecimalField(max_digits = 7, decimal_places = 5)
    long = models.DecimalField(max_digits = 8, decimal_places = 5)
    dr = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return "Device: {} | lat: {} - long: {}".format(self.device_id,self.lat,self.long)

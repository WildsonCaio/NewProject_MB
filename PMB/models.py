from django.db import models
from django.contrib.auth.models import User



class Register_Employeers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    photo = models.ImageField()
    def __str__(self):
        return self.name
        
class Register_Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    technique = models.TextField()
    products = models.CharField(max_length=255)
    professionals = models.ManyToManyField(Register_Employeers)
    def __str__(self):
        return self.name
        
class Register_Time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    def __str__(self):
        return self.date


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    employeers = models.ForeignKey(Register_Employeers, on_delete=models.CASCADE)        
    services = models.ForeignKey(Register_Services, on_delete=models.CASCADE)        
    time = models.ForeignKey(Register_Time, on_delete=models.CASCADE)        
           


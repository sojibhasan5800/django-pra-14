from django.db import models
from django.utils import timezone

# Create your models here.

class muscian_model(models.Model):
    instrument_type= [
       ('guitar','Guitar'),('flute','Flute'),('drum','Drum') 
    ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=20,choices=instrument_type,default=None)
    
    def __str__(self):
       return f"Name :{self.first_name} {self.last_name}"
    

    
class album_model(models.Model):
    rating_type=[
        ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'),
    ]
    album_name = models.CharField(max_length=20)
    realse_date = models.DateField(default=timezone.now)
    rating =models.CharField(max_length=20,choices=rating_type,default=0)
    relation = models.ForeignKey(muscian_model,on_delete=models.CASCADE)
    
    def __str__(self):
       return f"Albam_Name :{self.album_name} "





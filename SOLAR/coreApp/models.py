from django.db import models

# Create your models here.

class SocDoc(models.Model):
    stateOfCharge = models.CharField(max_length = 100)
    depthOfCharge = models.CharField(max_length = 100)
    timeStamp = models.CharField(max_length = 100)

    def __str__(self):
        return self.stateOfCharge + ' ' + self.depthOfCharge
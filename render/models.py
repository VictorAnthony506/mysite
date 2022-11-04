from django.db import models

# Create your models here.

class Operation(models.Model):
    # slackUsername = models.CharField(default="anthonyvictor385", max_length=255)
    operation_type = models.CharField(max_length=255)
    x = models.IntegerField()
    y = models.IntegerField()
    result = models.FloatField(default=0)
     
    def __str__(self):
        return self.operation_type
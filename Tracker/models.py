from django.db import models

# Create your models here.

class States(models.Model):
    State=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='states'
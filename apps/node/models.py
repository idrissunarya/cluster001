from django.db import models

class Departement(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

        def __str__(self):
            return self.name

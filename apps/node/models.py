from django.db import models

import uuid
from phone_field import PhoneField

class Departement(models.Model):
    departement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

        def __str__(self):
            return self.name


class Member(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact Phone number')
    address = models.TextField()
    photo = models.ImageField(upload_to='media/members/', default='media/members/default.jpg')

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25)

    age = property(age)



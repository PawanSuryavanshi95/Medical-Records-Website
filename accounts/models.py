from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PatientProfile(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class DoctorProfile(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    experience = models.IntegerField(help_text='Enter in years')

    def __str__(self):
        return self.firstname

class MedicalRecords(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    problem = models.TextField()
    date = models.DateTimeField('Date of Entry',default=timezone.now)
    illness = models.CharField(max_length=25,verbose_name='Major Illness Found')
    comment = models.TextField('''Doctor's Comment''')
    medicine = models.TextField()
    duration = models.IntegerField(default=None)
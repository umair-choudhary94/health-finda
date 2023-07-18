from django.db import models
from Registration.models import doctorProfile,PatientProfile
# Create your models here.
class Availability(models.Model):
    doctor = models.ForeignKey(doctorProfile, on_delete=models.CASCADE)
    available_date = models.DateField()
    available_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return str(self.available_date) + " " + str(self.available_time)
    def change_status(self, new_status):
        self.is_available = new_status
        self.save()
class Appointment(models.Model):
    availability = models.OneToOneField(Availability, on_delete=models.CASCADE,default=None)
    client = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    reason = models.TextField(default="Nothing")
    is_approved = models.BooleanField(default=False)
    def approve_now(self):
        if not self.is_approved:
            self.is_approved = True
            self.save()

class Notice(models.Model):
    doctor = models.ForeignKey(doctorProfile, on_delete=models.CASCADE)
    title = models.CharField(default="Nothing",max_length=1000)
    message = models.TextField(default="Nothing")
    timestamp = models.DateField()
    def __str__(self):
        return self.title
class Review(models.Model):
    doctor = models.ForeignKey(doctorProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    review = models.TextField(default="Nothing")
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.review
class Emergencycontact(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="Unknown")
    relation = models.CharField(max_length=200,default="Unknown")
    Contact = models.CharField(max_length=200,default="Unknown")

class Insuranceininfo(models.Model):
    patient =  models.OneToOneField(PatientProfile, on_delete=models.CASCADE,default=None)
    Insurancecarrier = models.CharField(max_length=200,default="Unknown")
    plan = models.CharField(max_length=200,default="Unknown")
    Contact = models.CharField(max_length=200,default="Unknown")
    policynumber = models.CharField(max_length=200,default="Unknown")
    groupnumber = models.CharField(max_length=200,default="Unknown")
    socialsecuritynumber = models.CharField(max_length=200,default="Unknown")
class healthinformation(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctorProfile, on_delete=models.CASCADE)
    note = models.CharField(max_length=200,default="Unknown")
    
    


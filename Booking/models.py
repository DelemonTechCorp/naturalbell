from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.username
class Room(models.Model):
    RoomNumber=models.CharField(max_length=50)
    def __str__(self):
        return self.RoomNumber
class Department(models.Model):
    Department=models.CharField(max_length=50)
    def str(self):
        return self.Department
class Treatment(models.Model):
    Treatment=models.CharField(max_length=50)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    def str(self):
        return self.Treatment

class Admin(models.Model):
    Lid=models.ForeignKey(Login,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    Image=models.ImageField(upload_to="images/",null=True)
    def __str__(self):
        return self.Name
class Doctor(models.Model):
    Lid=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    contact_no=models.BigIntegerField()
    email_id=models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    Speciality=models.CharField(max_length=50)
    About=models.TextField(null=True)
    DOB=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="images/",null=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Therapy(models.Model):
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Therapy=models.CharField(max_length=50)
    def __str__(self):
        return self.Therapy
class Status(models.Model):
    Status=models.CharField(max_length=100)
    color=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.Status
class Statusbooking(models.Model):
    Status=models.CharField(max_length=100)
    color=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.Status
class Patient(models.Model):
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=20, unique=True, editable=False,null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    DOB=models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    # here email is turned into nationality
    email = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    blood_gp=models.CharField(max_length=50,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    therapy=models.ForeignKey(Therapy,on_delete=models.CASCADE,null=True)
    treatment=models.ForeignKey(Treatment,on_delete=models.CASCADE,null=True)
    note=models.TextField(null=True)
    medicines=models.TextField(null=True)
    number_of_session=models.CharField(max_length=50,null=True)
    Followup =models.CharField(max_length=100,null=True)
    Proposedtreatmentplan=models.CharField(max_length=500,null=True)
    Treatment=models.CharField(max_length=100,null=True)
    Srothusinvolved=models.CharField(max_length=100,null=True)
    Dhathupredominence =models.CharField(max_length=100,null=True)
    Doshapredominence=models.CharField(max_length=100,null=True)
    Amanirama=models.CharField(max_length=100,null=True)
    Regularmedications=models.CharField(max_length=500,null=True)
    PastMedicalandsurgicalhistory=models.CharField(max_length=500,null=True)
    Historyofpresentingcomplaints  =models.CharField(max_length=500,null=True)
    Presentingcomplaints=models.CharField(max_length=500,null=True)
    Menstrualhistory=models.CharField(max_length=500,null=True)
    Allergies=models.CharField(max_length=500,null=True)
    Sleep=models.CharField(max_length=500,null=True)
    Digestion=models.CharField(max_length=500,null=True)
    Clinicaldetails=models.CharField(max_length=500,null=True)
    update_at= models.DateTimeField(auto_now_add=True, null=True)
    status=models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    Examinationfindings=models.CharField(max_length=500,null=True)
    Diagnosis=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.patient_id:  # Generate patient_id only if it doesn't exist
            self.patient_id = self.generate_unique_patient_id()
        super(Patient, self).save(*args, **kwargs)

    def generate_unique_patient_id(self):
        # Generate a unique ID with a specific format
        prefix = "PAT"
        unique_id = f"{prefix}{get_random_string(length=7).upper()}"
        while Patient.objects.filter(patient_id=unique_id).exists():
            unique_id = f"{prefix}{get_random_string(length=7).upper()}"
        return unique_id

class Therapist(models.Model):
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    specialization=models.ForeignKey(Therapy, on_delete=models.CASCADE)
    treatment=models.ForeignKey(Treatment,on_delete=models.CASCADE,null=True)
    contact_no=models.BigIntegerField()
    email_id=models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    Room=models.CharField(max_length=50,null=True)
    About=models.TextField(null=True)
    # DOB=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="media/images/", null=True)

    def __str__(self):
        return self.name
class booking(models.Model):
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment=models.ForeignKey(Treatment,on_delete=models.CASCADE,null=True)
    reg_date = models.DateField(null=True)
    reg_time = models.TimeField(null=True)
    about=models.TextField(null=True)
    status=models.ForeignKey(Statusbooking,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Schedule(models.Model):
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    patientid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    Therapy=models.ForeignKey(Therapy, on_delete=models.CASCADE)
    Note=models.TextField(null=True)
    Date=models.DateField()
    number_of_session=models.IntegerField()
    starting_Time=models.TimeField()
    ending_Time=models.TimeField()
    status=models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Note
class SessionStatus(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='sessions')
    session_number = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('not confirmed', 'Not Confirmed'), ('attended', 'Attended')], default='not confirmed')
    session_date = models.DateField(null=True, blank=True)
    starting_Time = models.TimeField(null=True, blank=True)  # New field
    ending_Time = models.TimeField(null=True, blank=True)
    session_group = models.IntegerField()
    class Meta:
        unique_together = ('schedule', 'session_number')

    def __str__(self):
        return f"Session {self.session_number}: {self.status}"

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations',null=True)
    Booking = models.ForeignKey(booking, on_delete=models.CASCADE,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True)
    consultation_date = models.DateTimeField(auto_now_add=True)
    medicines=models.TextField(null=True)
    number_of_session=models.CharField(max_length=50,null=True)
    Followup =models.CharField(max_length=100,null=True)
    Proposedtreatmentplan=models.CharField(max_length=100,null=True)
    Treatment=models.CharField(max_length=100,null=True)
    Srothusinvolved=models.CharField(max_length=100,null=True)
    Dhathupredominence =models.CharField(max_length=100,null=True)
    Doshapredominence=models.CharField(max_length=100,null=True)
    Amanirama=models.CharField(max_length=100,null=True)
    Regularmedications=models.CharField(max_length=500,null=True)
    PastMedicalandsurgicalhistory=models.CharField(max_length=500,null=True)
    Historyofpresentingcomplaints  =models.CharField(max_length=500,null=True)
    Presentingcomplaints=models.CharField(max_length=500,null=True)
    Menstrualhistory=models.CharField(max_length=500,null=True)
    Allergies=models.CharField(max_length=100,null=True)
    Sleep=models.CharField(max_length=100,null=True)
    Digestion=models.CharField(max_length=100,null=True)
    Clinicaldetails=models.CharField(max_length=500,null=True)
    update_at= models.DateTimeField(auto_now_add=True, null=True)
    status=models.ForeignKey(Statusbooking,on_delete=models.CASCADE,null=True)
    Examinationfindings=models.CharField(max_length=500,null=True)
    Diagnosis=models.CharField(max_length=100,null=True)
    therapy=models.ForeignKey(Therapy,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"Consultation on {self.consultation_date} for {self.patient.name}"



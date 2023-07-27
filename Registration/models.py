from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    user_type = models.CharField(max_length=10, default="nothing")
    is_verified = models.BooleanField(default=False)  

   

    def __str__(self):
        return self.user.username
class doctorProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    SPECIALIZATION_CHOICES = [
        ('p_general-practitioner', 'General Practitioner'),
        ('p_dentist', 'Dentist'),
        ('p_therapeutic-reflexologist', 'Therapeutic Reflexologist'),
        ('p_acoustician-hearing-aid', 'Acoustician (Hearing Aid)'),
        ('p_aesthetic-practitioner', 'Aesthetic Practitioner'),
        ('p_aesthetic-and-wellness', 'Aesthetic and Wellness'),
        ('p_allergy-specialist', 'Allergy Specialist'),
        ('p_anaesthesiologist', 'Anaesthesiologist'),
        ('p_anaesthetist', 'Anaesthetist'),
        ('p_audiologist', 'Audiologist'),
        ('p_baby-clinic', 'Baby Clinic'),
        ('p_biokineticist', 'Biokineticist'),
        ('p_cardiologist', 'Cardiologist'),
        ('p_chiropractor', 'Chiropractor'),
        ('p_clinic', 'Clinic'),
        ('p_clinical-haematologist', 'Clinical Haematologist'),
        ('p_clinical-neurophysiologist', 'Clinical Neurophysiologist'),
        ('p_clinical-nurse', 'Clinical Nurse'),
        ('p_clinical-pathologist', 'Clinical Pathologist'),
        ('p_clinical-practitioner', 'Clinical Practitioner'),
        ('p_clinical-psychologist', 'Clinical Psychologist'),
        ('p_clinical-services', 'Clinical Services'),
        ('p_clinical-social-worker', 'Clinical Social Worker'),
        ('p_clinical-technologist', 'Clinical Technologist'),
        ('p_clinical-technologist-pulmonology', 'Clinical Technologist - Pulmonology'),
        ('p_colon-hydrotherapist', 'Colon Hydrotherapist'),
        ('p_counselling-psychologist', 'Counselling Psychologist'),
        ('p_counsellor', 'Counsellor'),
        ('p_dental-surgeon', 'Dental Surgeon'),
        ('p_dental-therapist', 'Dental Therapist'),
        ('p_dentistry', 'Dentistry'),
        ('p_dermatologist', 'Dermatologist'),
        ('p_dietician', 'Dietician'),
        ('p_dietician-nutritionist', 'Dietician / Nutritionist'),
        ('p_doctor', 'Doctor'),
        ('p_ear-nose-throat-specialist', 'Ear, Nose & Throat Specialist'),
        ('p_educational-psychologist', 'Educational Psychologist'),
        ('p_endocrinologist', 'Endocrinologist'),
        ('p_family-physician', 'Family Physician'),
        ('p_family-practice', 'Family Practice'),
        ('p_forensic-psychologist', 'Forensic Psychologist'),
        ('p_functional-medicine-practitioner', 'Functional Medicine Practitioner'),
        ('p_gp', 'GP'),
        ('p_gastroenterologist', 'Gastroenterologist'),
        ('p_general-practice', 'General Practice'),
        ('p_general-surgeon', 'General Surgeon'),
        ('p_genetic-counsellor', 'Genetic Counsellor'),
        ('p_group-practice-multi-disciplinary', 'Group Practice: Multi Disciplinary'),
        ('p_gynaecologist', 'Gynaecologist'),
        ('p_hiv-clinician', 'HIV Clinician'),
        ('p_haematology', 'Haematology'),
        ('p_head-and-neck-surgeon', 'Head and Neck Surgeon'),
        ('p_health-and-wellness-coach', 'Health and Wellness Coach'),
        ('p_hearing-aid-acoustician', 'Hearing Aid Acoustician'),
        ('p_homeopath', 'Homeopath'),
        ('p_integrative-general-practitioner', 'Integrative General Practitioner'),
        ('p_integrative-medicine-practitioner', 'Integrative Medicine Practitioner'),
        ('p_interventional-radiologist', 'Interventional Radiologist'),
        ('p_lab-diagnostics', 'Lab Diagnostics'),
        ('p_life-coach', 'Life Coach'),
        ('p_live-blood-analysis-practitioner', 'Live Blood Analysis Practitioner'),
        ('p_live-blood-analyst', 'Live Blood Analyst'),
        ('p_marriage-counsellor', 'Marriage Counsellor'),
        ('p_maxillo-facial-and-oral-surgery', 'Maxillo Facial And Oral Surgery'),
        ('p_maxillofacial-surgeon', 'Maxillofacial Surgeon'),
        ('p_medical-oncologist', 'Medical Oncologist'),
        ('p_medical-technologist', 'Medical Technologist'),
        ('p_midwife', 'Midwife'),
        ('p_nephrologist', 'Nephrologist'),
        ('p_neurologist', 'Neurologist'),
        ('p_neuropsychologist', 'Neuropsychologist'),
        ('p_neurosurgeon', 'Neurosurgeon'),
        ('p_nurse', 'Nurse'),
        ('p_obstetrician', 'Obstetrician'),
        ('p_obstetrics-and-gynaecologist', 'Obstetrics And Gynaecologist'),
        ('p_occupational-health-nurse-practitioner', 'Occupational Health Nurse Practitioner'),
        ('p_occupational-health-physician', 'Occupational Health Physician'),
        ('p_occupational-practitioner', 'Occupational Practitioner'),
        ('p_occupational-therapist', 'Occupational Therapist'),
        ('p_oncologist', 'Oncologist'),
        ('p_ophthalmologist', 'Ophthalmologist'),
        ('p_optometrist', 'Optometrist'),
        ('p_oral-hygienist', 'Oral Hygienist'),
        ('p_orthodontist', 'Orthodontist'),
        ('p_orthopaedic-surgeon', 'Orthopaedic Surgeon'),
        ('p_orthotist-prosthetist', 'Orthotist & Prosthetist'),
        ('p_otolaryngologist', 'Otolaryngologist'),
        ('p_paediatric-dermatologist', 'Paediatric Dermatologist'),
        ('p_paediatric-general-practitioner', 'Paediatric General Practitioner'),
        ('p_paediatric-surgeon', 'Paediatric Surgeon'),
        ('p_paediatrician', 'Paediatrician'),
        ('p_periodontist', 'Periodontist'),
        ('p_physician', 'Physician'),
        ('p_physiotherapist', 'Physiotherapist'),
        ('p_plastic-surgeon', 'Plastic Surgeon'),
        ('p_podiatrist', 'Podiatrist'),
        ('p_primary-care-physician', 'Primary Care Physician'),
        ('p_primary-healthcare-clinic', 'Primary Healthcare Clinic'),
        ('p_primary-healthcare-nurse', 'Primary Healthcare Nurse'),
        ('p_prosthodontist', 'Prosthodontist'),
        ('p_psychiatrist', 'Psychiatrist'),
        ('p_psychologist', 'Psychologist'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES, default="")
    qualifications = models.CharField(max_length=200, default="")
    experience = models.PositiveIntegerField(default=0)
    contact_number = models.CharField(max_length=15, default="")
    email = models.EmailField(default="")
    address = models.CharField(max_length=100, default="")
    biography = models.TextField(default="")
    languages_spoken = models.CharField(max_length=100, default="")
    hospital_affiliations = models.CharField(max_length=200, default="")
    profile_pic = models.ImageField(upload_to='doctor_profile_pics/', default="default.jpg")
    latitude = models.CharField(max_length=100,default="0000")
    longitude = models.CharField(max_length=100,default="0000")
    @property
    def get_formatted_specialization_display(self):
        return self.specialization[2:].capitalize() if self.specialization.startswith('p_') else self.specialization
    def __str__(self):
        return self.user.username
    

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )

    address = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=20, default="")
    medical_conditions = models.TextField(default="")
    surgeries = models.TextField(default="")
    medications = models.TextField(default="")
    allergies = models.TextField(default="")
    occupation = models.CharField(max_length=100, default="")
    exercise_habits = models.CharField(max_length=100, default="")
    dietary_restrictions = models.CharField(max_length=100, default="")
    family_medical_history = models.TextField(default="")
    age = models.PositiveIntegerField(default=0)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default="")
    profile_pic = models.ImageField(upload_to='profile_pics/', default="default.jpg")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    city = models.CharField(max_length=100,default="Unknown")
    state = models.CharField(max_length=100,default="AZ")
    zip_code = models.CharField(max_length=100,default="Unknown")

    def __str__(self):
        return self.user.username
    

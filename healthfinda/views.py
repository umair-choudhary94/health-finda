from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from Registration.models import doctorProfile, PatientProfile
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    specialization_choices = doctorProfile.SPECIALIZATION_CHOICES

    context = {
        'specialization_choices': specialization_choices
    }

    return render(request, 'pages/home.html', context)
def contact_submit(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('c_fname')
        last_name = request.POST.get('c_lname')
        email = request.POST.get('c_email')
        subject = request.POST.get('c_subject')
        message = request.POST.get('c_message')
        
      
        
        # Specify the list of additional email recipients
        additional_recipients = ['umairsabirjutt@gmail.com',"sydtalks42@gmail.com"]

        # Build the email body
        email_body = f'Name: {first_name}\nEmail: {email}\nMessage: {message}'

        # Combine the additional recipients list with the default email sender
        recipients = [settings.DEFAULT_FROM_EMAIL] + additional_recipients

        # Send the email to all recipients
        send_mail(
            subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            recipients,
            fail_silently=False,
        )
        
        # Optionally, you can save the form data to a database or perform other actions
        
        # Return a response indicating the form submission was successful
        return render(request, 'pages/success.html')
    else:
        # Handle GET requests or other methods if needed
        return render(request, 'pages/contact.html')
    
def about(request):
    return render(request,"pages/about.html")



@login_required(login_url='/registration/login/') 
def profile(request):
    user = request.user

    if user.userprofile.user_type == 'doctor':
        try:
            profile = doctorProfile.objects.get(user=user)
            availabilities = Availability.objects.filter(doctor=profile)
            Appointments = Appointment.objects.filter(availability__doctor=profile)
            notices = Notice.objects.filter(doctor=profile)
            reviews = Review.objects.filter(doctor=profile)
            context = {
                "profile" : profile,
                "availabilities" : availabilities,
                "Appointments" : Appointments,
                "notices" : notices,
                "reviews" : reviews
            }
            return render(request, 'pages/doctor_profile.html',context)
        except:
            return redirect("create_doctor_profile")
        

    elif user.userprofile.user_type == 'patient':
        try:
            profile = PatientProfile.objects.get(user=user)
            Appointments = Appointment.objects.filter(client=profile)
            try:
                insurance = Insuranceininfo.objects.get(patient=profile)
            except:
                return redirect("addinsuranceinfo")
            emergency_contacts = Emergencycontact.objects.filter(patient=profile)
            context = {
                "profile" : profile,
                "Appointments" :  Appointments,
                "insurance": insurance,
                "emergency_contacts" : emergency_contacts,
            }
            return render(request, 'pages/patient_profile.html',context)
        except:
            return redirect("create_patient_profile")
        # return render(request, 'pages/patient_profile.html')

    else:
        # Handle other user types or error cases
        return render(request, 'pages/unknown_user.html')
@login_required(login_url='/registration/login/') 
def create_patient_profile(request):
    
    try:
        profile = PatientProfile.objects.get(user=request.user)
        return redirect("profile")
    except:
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
        if request.method == 'POST':
            
            address = request.POST.get('address')
            phone_number = request.POST.get('phone_number')
            age = request.POST.get('age')
            blood_group = request.POST.get('blood_group')
            gender = request.POST.get('gender')
            profile_pic = request.FILES.get('profile_pic')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            medical_conditions = request.POST.get('medical_conditions')
            surgeries = request.POST.get('surgeries')
            medications = request.POST.get('medications')
            allergies = request.POST.get('allergies')
            occupation = request.POST.get('occupation')
            exercise_habits = request.POST.get('exercise_habits')
            dietary_restrictions = request.POST.get('dietary_restrictions')
            family_medical_history = request.POST.get('family_medical_history')

            profile = PatientProfile(
                user= request.user,
                address=address,
                phone_number=phone_number,
                age=age,
                blood_group=blood_group,
                gender=gender,
                profile_pic=profile_pic,
                weight=weight,
                height=height,
                medical_conditions=medical_conditions,
                surgeries=surgeries,
                medications=medications,
                allergies=allergies,
                occupation=occupation,
                exercise_habits=exercise_habits,
                dietary_restrictions=dietary_restrictions,
                family_medical_history=family_medical_history
            )
            profile.save()
            return redirect('profile')  # Redirect to the desired page after profile creation
        context = {
            'GENDER_CHOICES': GENDER_CHOICES,
            'BLOOD_GROUP_CHOICES': BLOOD_GROUP_CHOICES
        }
        return render(request, 'pages/createpatientprofile.html',context)
    


def create_doctor_profile(request):
    GENDER_CHOICES = doctorProfile.GENDER_CHOICES
    SPECIALIZATION_CHOICES = doctorProfile.SPECIALIZATION_CHOICES
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        specialization = request.POST.get('specialization')
        qualifications = request.POST.get('qualifications')
        experience = request.POST.get('experience')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        biography = request.POST.get('biography')
        languages_spoken = request.POST.get('languages_spoken')
        hospital_affiliations = request.POST.get('hospital_affiliations')
        profile_pic = request.FILES.get('profile_pic')

        # Create the doctorProfile object
        doctor = doctorProfile(
            user = request.user,
            name=name,
            gender=gender,
            specialization=specialization,
            qualifications=qualifications,
            experience=experience,
            contact_number=contact_number,
            email=email,
            address=address,
            biography=biography,
            languages_spoken=languages_spoken,
            hospital_affiliations=hospital_affiliations,
            profile_pic=profile_pic
        )
        doctor.save()

        # Redirect to a success page or render a success message
        return redirect('profile')
    context = {
        'GENDER_CHOICES': GENDER_CHOICES,
        'SPECIALIZATION_CHOICES': SPECIALIZATION_CHOICES
    }
    return render(request, 'pages/createdoctorprofile.html',context)

def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.approve_now()
    appointment.availability.change_status(False)
    # Perform any additional actions or redirect to a success page
    return redirect("profile")

def search_doctors(request):
    speciality = request.GET.get('speciality')
    address = request.GET.get('address')
    name = request.GET.get('name')

    doctors = doctorProfile.objects.all()

    if speciality:
        doctors = doctors.filter(Q(specialization__icontains=speciality))
    if address:
        doctors = doctors.filter(Q(address__icontains=address))
    if name:
        doctors = doctors.filter(Q(name__icontains=name))

    context = {'doctors': doctors}
    return render(request, 'pages/search_results.html', context)
def getdoctor(request,name):
    profile = doctorProfile.objects.get(name=name)
    availabilities = Availability.objects.filter(doctor=profile,is_available=True)
    notices = Notice.objects.filter(doctor=profile)
    reviews = Review.objects.filter(doctor=profile)
    context = {
                
        "availabilities" : availabilities,
        'profile': profile,
        "notices" : notices,
        "reviews" : reviews
                
    }
    return render(request,"pages/doctorappointment.html",context)
def getpatient(request,id):
    print("Entering")
    profile = PatientProfile.objects.get(user=id)
    Appointments = Appointment.objects.filter(client=profile)
    
    insurance = Insuranceininfo.objects.get(patient=profile)
    
    emergency_contacts = Emergencycontact.objects.filter(patient=profile)
    healthinfo = healthinformation.objects.filter(patient=profile)
    context = {
        "profile" : profile,
        "Appointments" :  Appointments,
        "insurance": insurance,
        "emergency_contacts" : emergency_contacts,
        "healthinfo" : healthinfo
    }
    return render(request,"pages/public_patient_profile.html",context)
@login_required(login_url='/registration/login/') 
def makeappointment(request,id):
    avail = Availability.objects.get(id=id)
    
    if request.method == "POST":
        reason = request.POST["reason"]
        user = request.user
        subject = "Appointment Booking"
        # Specify the list of additional email recipients
        additional_recipients = [user.email]

        # Build the email body
        email_body = f'Your request for appointment booking is under review'

        # Combine the additional recipients list with the default email sender
        recipients = [settings.DEFAULT_FROM_EMAIL] + additional_recipients

        # Send the email to all recipients
        send_mail(
            subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            recipients,
            fail_silently=False,
        )
        
        profile = PatientProfile.objects.get(user=user.id)
        obj = Appointment(availability=avail,reason=reason,client=profile)
        obj.save()
        return redirect("profile")
    context = {
        "avail" : avail,
        "id" : id,
    }
    return render(request,"pages/makeappointment.html",context)
def addnotice(request,name):

    if request.method == "POST":
        
        title = request.POST["title"]
        message = request.POST["message"]
        date = request.POST["date"]
        profile = doctorProfile.objects.get(name=name)
        obj = Notice(doctor=profile,title=title,message=message,timestamp=date)
        obj.save()
        return redirect("profile")
def addreview(request,name):

    if request.method == "POST":
        
        
        review = request.POST["review"]
        
        profile = doctorProfile.objects.get(name=name)
        user = request.user
        client = PatientProfile.objects.get(user=user.id)
        obj = Review(doctor=profile,client=client,review=review)
        obj.save()
        return redirect(f"/doctor/{name}/")
def addavailablity(request,name):

    if request.method == "POST":
        
        
        date = request.POST["date"]
        time = request.POST["time"]
        profile = doctorProfile.objects.get(name=name)
        
        obj = Availability(doctor=profile,available_date=date,available_time=time)
        obj.save()
        return redirect("profile")
    
def addinsuranceinfo(request):
    if request.method == "POST":
        
        Insurancecarrier = request.POST["Insurancecarrier"]
        plan = request.POST["plan"]
        Contact = request.POST["Contact"]
        policynumber = request.POST["policynumber"]
        groupnumber = request.POST["groupnumber"]
        
        user = request.user
        profile = PatientProfile.objects.get(user=user.id)
        
        obj = Insuranceininfo(patient=profile,Insurancecarrier=Insurancecarrier,plan=plan,Contact=Contact,policynumber=policynumber,groupnumber=groupnumber)
        obj.save()
        return redirect("profile")
    return render(request,"pages/addinsuranceinfo.html")
def addcontactinfo(request):
    if request.method == "POST":
        
        name = request.POST["name"]
        relation = request.POST["relation"]
        Contact = request.POST["Contact"]
        
        user = request.user
        profile = PatientProfile.objects.get(user=user.id)
        
        obj = Emergencycontact(patient=profile,name=name,relation=relation,Contact=Contact)
        obj.save()
        return redirect("profile")
    return redirect("profile")
def addnote(request):
    if request.method == "POST":
        
        note = request.POST["note"]
        patient = request.POST["patient"]
        user = request.user
        doctor = doctorProfile.objects.get(user=user)
        
        patientt = PatientProfile.objects.get(user=patient)
        
        obj = healthinformation(patient=patientt,doctor=doctor,note=note)
        obj.save()
        print(patient)
        return redirect(f"/patient/{patient}/")



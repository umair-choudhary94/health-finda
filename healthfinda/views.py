from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"pages/home.html")
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
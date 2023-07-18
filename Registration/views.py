from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str,force_bytes

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST['user_type']

        # Perform any additional validation or processing here
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password1, email=email,
                                        first_name=first_name, last_name=last_name)
        
        # Create a user profile
        profile = UserProfile(user=user, user_type=user_type)
        profile.save()
        # Send verification email
        # current_site = get_current_site(request)
        # mail_subject = 'Activate your account'
        # message = render_to_string('user/verification_email.html', {
        #     "msg" : "Welcom to Health Finda",
        # })
        # send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [email])

            # Redirect to a success page or perform any additional actions
        return redirect('login')  # Change 'verification_sent' to the desired URL name

        # Redirect to a success page or perform any additional actions

    return render(request, 'user/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user
            login(request, user)
            # Redirect to a success page or perform any additional actions
            return redirect('/profile')  # Change 'home' to the desired URL name
        else:
            # Handle authentication failure (e.g., show an error message)
            error_message = 'Invalid username or password'
            return render(request, 'user/login.html', {'error_message': error_message})

    return render(request, 'user/login.html')
def logout_view(request):
    logout(request)
    return redirect('home')

def verify_email(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        # Handle invalid verification link (e.g., show an error message)
        error_message = 'Invalid verification link'
        return render(request, 'user/verification_failed.html', {'error_message': error_message})

    if default_token_generator.check_token(user, token):
        # Update the verification status of the user
        user.profile.is_verified = True
        user.profile.save()

        # Redirect to a success page or perform any additional actions
        return redirect('home')  # Change 'verification_success' to the desired URL name
    else:
        # Handle invalid verification link (e.g., show an error message)
        error_message = 'Invalid verification link'
        return render(request, 'user/verification_failed.html', {'error_message': error_message})
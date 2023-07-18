from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # Generate verification code
        verification_code = User.objects.make_random_password(length=6)

        # Add the verification code to the cleaned_data
        cleaned_data['verification_code'] = verification_code

        return cleaned_data

    def send_verification_email(self, cleaned_data):
        username = cleaned_data['username']
        verification_code = cleaned_data['verification_code']
        email = cleaned_data['email']

        subject = 'Verification Code'
        message = f'Hello {username},\n\nYour verification code is: {verification_code}'
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, message, from_email, [email], fail_silently=False)

from django.contrib import admin
from .models import UserProfile,PatientProfile,doctorProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type',"is_verified")




@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'age', 'blood_group', 'gender')
    list_filter = ('blood_group', 'gender')
    search_fields = ('user__username', 'user__email', 'address', 'phone_number')

    # Additional customization options
    ordering = ('user__username',)
    list_per_page = 20
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'address', 'phone_number','profile_pic')
        }),
        ('Medical Information', {
            'fields': ('age', 'blood_group', 'medical_conditions', 'surgeries', 'medications', 'allergies')
        }),
        ('Personal Information', {
            'fields': ('gender', 'weight', 'height', 'occupation', 'exercise_habits', 'dietary_restrictions', 'family_medical_history')
        }),
    )

class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'specialization', 'experience', 'contact_number', 'email']
    list_filter = ['gender', 'specialization']
    search_fields = ['name', 'specialization', 'email']

admin.site.register(doctorProfile, DoctorProfileAdmin)
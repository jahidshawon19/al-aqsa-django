from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields = [
            'course_title',
            'category',
            'durations',
            'overview',
            'thumbnail_image',
            'video',
            'popular'
        ] 

class CreateRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'

        ] 



class CreateTutorForm(forms.ModelForm):
    class Meta:
        model = Tutor 
        fields = [
            'email',
            'phone',
            'details',
            'achievement',
            'photo'
        ] 



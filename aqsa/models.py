from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,EmailInput
# Create your models here.


class Setting(models.Model):
    header_logo = models.ImageField(blank=True, upload_to='logo/')
    footer_logo = models.ImageField(blank=True, upload_to='logo/')
    short_description = models.TextField()
    helpline = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=150)
    official_mail=models.CharField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
    photo = models.ImageField(blank=True, upload_to='about/')
    details = models.TextField() 
    chooseUs = models.TextField() 
    mission = models.TextField() 
    vission = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class Slider(models.Model):
    banner_image = models.ImageField(blank=True, upload_to='banner/')
    heading = models.CharField(blank=True, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

class Testimonial(models.Model):
    client_image = models.ImageField(blank=True, upload_to='testimonial/')
    client_name = models.CharField(blank=True, max_length=150)
    designation = models.CharField(blank=True, max_length=150)
    testimonial_data = models.TextField()

    def __str__(self):
        return self.client_name

class Sponsor(models.Model):
    photo = models.ImageField(blank=True, upload_to='spons/')



class Tutor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=15)
    details = models.TextField(blank=True)
    achievement = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='tutor_images/')
    facebook = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    twitter = models.URLField(blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.username
        



class CourseCategory(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    


class Course(models.Model):
    instructor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=150)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    durations = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail_image = models.ImageField(blank=True, upload_to='course_thumnail/')
    video = models.FileField(upload_to='videos/', blank=True)
    popular = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.course_title




class Contact(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name     


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject','phone','message']
        widgets = {
            'name':TextInput(attrs={'class':'input', 'placeholder':'Enter Your Name'}),
            'email':EmailInput(attrs={'class':'input', 'placeholder':'Enter Your Email'}),
            'subject':EmailInput(attrs={'class':'input', 'placeholder':'Enter Your Subject'}),
            'phone':EmailInput(attrs={'class':'input', 'placeholder':'Enter Your Phone'}),
            'message':TextInput(attrs={'class':'input', 'placeholder':'Message'}),
        }
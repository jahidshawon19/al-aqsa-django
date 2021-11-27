from django.urls import path 
from .views import *
urlpatterns=[
    path('', homePage, name="index"),
    path('about/', aboutPage, name="about-us"),
    path('courses/', allCourse, name="all-course"),
    path('courses/<int:id>/', singleCourse, name="single-course"),
    path('category/<name>/', getCategory, name="course-category"),
    path('teachers/', allTeacher, name="all-teacher"),
    path('teacher_profile/<name>/', getTutor, name="tutor"),

    path('login/',getLogin, name="login"),
    path('logout/',getLogout, name="logout"),

    path('create/', getCreate, name="create"),
    path('upadate/<int:id>/', updateCourse, name="update-course"),
    path('delete/<int:id>/', deleteCourse, name="delete-course"),

    path('profile/', getProfile, name="instructor-profile"),
    path('register/', getRegister, name="register"),

    path('contact/', contactPage, name="contact-us")
    
]
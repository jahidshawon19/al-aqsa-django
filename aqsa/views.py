
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    settings_data = get_object_or_404(Setting, id=1)
    slider_data = Slider.objects.all().order_by('-id')[:3]
    testimonial_data = Testimonial.objects.all()
    sponsorship = Sponsor.objects.all()
    top_rated_course = Course.objects.all().order_by('-id')[:4]  
    home_teacher = Tutor.objects.all().order_by('-id')[:4]
    context = {
        'top_rated_course':top_rated_course,    
        'home_teacher':home_teacher,
        'settings_data':settings_data,
        'slider_data':slider_data,
        'testimonial_data':testimonial_data,
        'sponsorship':sponsorship,
    }
    return render(request, "index.html", context)

def aboutPage(request):
    settings_data = get_object_or_404(Setting, id=1)
    testimonial_data = Testimonial.objects.all()
    sponsorship = Sponsor.objects.all()
    data = get_object_or_404(About, id=1)
    context = {
        'data':data,
        'settings_data':settings_data,
        'testimonial_data':testimonial_data,
        'sponsorship':sponsorship,
    }
    return render(request, "about.html", context)



def allCourse(request):
    settings_data = get_object_or_404(Setting, id=1)
    course = Course.objects.all()
    search = request.GET.get('q')
    if search:
        course = course.filter(
            Q(course_title__icontains=search)
        )

    context = {
        'course':course,
        'settings_data':settings_data,
        

    }
    return render(request, "courses.html", context)

def singleCourse(request,id):
    settings_data = get_object_or_404(Setting, id=1)
    course = get_object_or_404(Course, pk=id)
    related_course = Course.objects.filter(category=course.category).exclude(id=id)[:8]
    context = {
        'course':course,
        'related_course':related_course,
        "settings_data":settings_data,
    }
    return render(request, "courses-singel.html", context)

       
def getCategory(request, name):
    settings_data = get_object_or_404(Setting, id=1)
    cat = get_object_or_404(CourseCategory, name=name)
    course = Course.objects.filter(category=cat.id)
    context = {
        'cat':cat,
        'course':course,
        "settings_data":settings_data,
    }
    return render(request, "category.html", context)


def allTeacher(request):
    settings_data = get_object_or_404(Setting, id=1)
    teacher_data = Tutor.objects.all()
    total_teacher = teacher_data.count()
    context = {
        'teacher_data':teacher_data,
        'total_teacher':total_teacher,
        "settings_data":settings_data,
    }
    return render(request, "teachers.html", context)

def getTutor(request, name):
    settings_data = get_object_or_404(Setting, id=1)
    course_teacher = get_object_or_404(User, username=name)
    auth = get_object_or_404(Tutor, name=course_teacher)
    course = Course.objects.filter(instructor=auth.id)
    context = {
        'course_teacher':course_teacher,
        'auth':auth,
        'course':course,
        "settings_data":settings_data,
    }
    return render(request, "teachers-singel.html", context)


def getLogin(request):
    settings_data = get_object_or_404(Setting, id=1)
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    
    return render(request, "login.html", {"settings_data":settings_data})


def getLogout(request):
    logout(request)
    return redirect('login')

@login_required
def getCreate(request):
    settings_data = get_object_or_404(Setting, id=1)
    u = get_object_or_404(Tutor, name= request.user.id)
    form = CreateCourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.instructor = u
        instance.save();
        return redirect('all-course')
    context = {
        'form':form,
        "settings_data":settings_data,
    }
    return render(request, "create.html", context)

@login_required
def updateCourse(request,id):
    settings_data = get_object_or_404(Setting, id=1)
    u = get_object_or_404(Tutor, name= request.user.id)
    course = get_object_or_404(Course, id=id)
    form = CreateCourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.instructor = u
        instance.save();
        return redirect('instructor-profile')
    context = {
        'form':form,
        "settings_data":settings_data,
    }
    return render(request, "create.html", context)    

@login_required
def deleteCourse(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('instructor-profile')



@login_required
def getProfile(request):
    settings_data = get_object_or_404(Setting, id=1)
    teacher = get_object_or_404(User, id = request.user.id)
    teacher_profile = Tutor.objects.filter(name=teacher.id)
    if teacher_profile:
        tutor_user = get_object_or_404(Tutor, name=request.user.id)
        course = Course.objects.filter(instructor=tutor_user.id)
        return render(request, 'profile.html', {"course":course, "tutor_user":tutor_user, "settings_data":settings_data,})
    else:
        form = CreateTutorForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name=teacher
            instance.save()
            return redirect('instructor-profile')
        return render(request, 'create_tutor.html', {"form":form, "settings_data":settings_data,})



def getRegister(request):
    settings_data = get_object_or_404(Setting, id=1)
    form = CreateRegisterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    context = {
        'form':form,
        'settings_data':settings_data,
    }
    return render(request, "register.html", context)



def contactPage(request):
    settings_data = get_object_or_404(Setting, id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.save()
            return redirect('index')
    form = ContactForm
    context = {
        'settings_data':settings_data,
        'form':form,
    }
    return render(request, "contact.html", context)
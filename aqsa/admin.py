from django.contrib import admin
from .models import *
# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['name', 'phone']
    search_fields = ['phone']
 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']    
    list_filter = ['name']
    search_fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title','instructor', 'created_at']
    list_filter = ['course_title']
    search_fields = ['course_title']   


admin.site.register(Setting) 
admin.site.register(About) 
admin.site.register(Slider)
admin.site.register(Testimonial)
admin.site.register(Sponsor)   
admin.site.register(Contact)
admin.site.register(Tutor,TutorAdmin)  
admin.site.register(CourseCategory,CategoryAdmin)  
admin.site.register(Course,CourseAdmin)  

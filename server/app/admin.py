from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UniversityAdmin(admin.ModelAdmin):
    model = University
    list_display = ('name', 'name_short', 'name_en', 'name_en_short',)


class UndergraduateAdmin(admin.ModelAdmin):
    model = Undergraduate
    list_display = ('name', 'university',)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'undergraduate',)


class FacultyAdmin(admin.ModelAdmin):
    model = Faculty
    list_display = ('name', 'age', 'email', 'phone', 'belong',)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('name', 'faculty',)



class CourseEvaluationAdmin(admin.ModelAdmin):
    model = CourseEvaluation
    list_display = ('course', 'pnc', 'description',)


class EvaluationRecordAdmin(admin.ModelAdmin):
    model = EvaluationRecord
    list_display = ('evaluation', 'user', 'score',)
    

# UserAdmin 재등록
admin.site.register(University, UniversityAdmin)
admin.site.register(Undergraduate, UndergraduateAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseEvaluation, CourseEvaluationAdmin)
admin.site.register(EvaluationRecord, EvaluationRecordAdmin)

from django.contrib import admin

from .models import ProfessorModel
from . models import StudentModel
from .models import SubjectModel
from .models import SubjectGradesModel

class ProfessorModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('title',)
    readonly_fields = ('title',)

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'professor', 'academic_year')
    list_filter = ('academic_year',)
    search_fields = ('name',)

class SubjectGradesModelAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'score',)
    search_fields = ('subject__name', 'student__name',)
    list_filter = ('subject',)

admin.site.register(ProfessorModel, ProfessorModelAdmin)
admin.site.register(StudentModel, StudentModelAdmin)
admin.site.register(SubjectModel, SubjectModelAdmin)
admin.site.register(SubjectGradesModel, SubjectGradesModelAdmin)

# Register your models here.

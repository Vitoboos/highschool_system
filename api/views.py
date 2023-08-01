from django.shortcuts import render
from rest_framework import viewsets
from .serializer import StudentModelSerializer, ProfessorModelSerializer, SubjectModelSerializer, SubjectGradesModelSerializer
from .models import StudentModel, ProfessorModel, SubjectGradesModel, SubjectModel

# Create your views here.

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        student_name = self.request.query_params.get('name', None)
        academic_year = self.request.query_params.get('academic_year', None)
        if student_name is not None:
            queryset = queryset.filter(name=student_name)
        if academic_year is not None:
            queryset = queryset.filter(academic_year=academic_year)
        return queryset

class ProfessorModelViewset(viewsets.ModelViewSet):
    queryset = ProfessorModel.objects.all()
    serializer_class = ProfessorModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        professor_name = self.request.query_params.get('name', None)
        if professor_name is not None:
            queryset = queryset.filter(name=professor_name)
        return queryset

class SubjectModelViewset(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectModelSerializer

    def get_queryset(self):

        # Filter by Professor 
        queryset = self.queryset
        professor_id = self.request.query_params.get('professor_id', None)
        subject_name = self.request.query_params.get('name', None)
        academic_year  = self.request.query_params.get('academic_year', None)

        if professor_id is not None:
            queryset = queryset.filter(professor_id=professor_id)

        if subject_name is not None:
            queryset = queryset.filter(name=subject_name)

        if academic_year is not None:
            queryset = queryset.filter(academic_year=academic_year)

        return queryset 


class SubjectGradesModelViewset(viewsets.ModelViewSet):
    queryset = SubjectGradesModel.objects.all()
    serializer_class = SubjectGradesModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        student_name = self.request.query_params.get('student', None)
        subject_id = self.request.query_params.get('subject', None)
        if student_name is not None:
            queryset = queryset.filter(student=student_name)

        if subject_id is not None:
            queryset = queryset.filter(subject=subject_id)

        return queryset

def grades_view(request):
 
    # Pass the records to the template for rendering
    return render(request, 'grades.html')
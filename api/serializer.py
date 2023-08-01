from rest_framework import serializers
from .models import StudentModel, ProfessorModel, SubjectModel, SubjectGradesModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

class ProfessorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorModel
        fields = '__all__'


class SubjectModelSerializer(serializers.ModelSerializer):
    professor_name = serializers.SerializerMethodField()

    class Meta:
        model = SubjectModel
        fields = '__all__'
    
    def get_professor_name(self, obj):
        return (obj.professor.name)

class SubjectGradesModelSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    subject_tag = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = SubjectGradesModel
        fields = '__all__'

    def get_subject_name(self, obj):
        return (obj.subject.name)
    
    def get_subject_tag(self, obj):
        return (obj.subject.tag)
    
    def get_student_name(self, obj):
        return (obj.student.name)

from django.db import models

class ProfessorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    academic_year = models.IntegerField()
    title = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        
            if self.academic_year == 8:
                self.title = 'Eight Grade'
            elif self.academic_year == 9:
                self.title = 'Freshman'
            elif self.academic_year == 10:
                self.title = 'Sophomore'
            elif self.academic_year == 11:
                self.title = 'Junior'
            else:
                self.title = 'Senior'

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name 
    
class SubjectModel(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=4, default='0000')
    professor = models.ForeignKey(ProfessorModel, on_delete=models.CASCADE, default="")
    academic_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class SubjectGradesModel(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    period1 = models.FloatField()
    period2 = models.FloatField()
    period3 = models.FloatField()
    score =  models.FloatField()
    approved = models.BooleanField()

    def save(self, *args, **kwargs):
            self.score = self.period1 + self.period2 + self.period3
            if self.score >= 150:
                self.approved = True
            else:
                self.approved = False
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.subject) + " : " + str(self.student) 
    

# Create your models here.

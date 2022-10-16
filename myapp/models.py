from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vacancy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    qualifications = models.TextField()
    responsbilities = models.TextField()
    deadline=models.DateTimeField()
    
    def __str__(self):
       return self.job_title
       
class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy,max_length=100,on_delete=models.CASCADE)
    experience = models.TextField()
    highest_qualification = models.CharField(max_length=100)
    school = models.CharField(max_length=1000)
    about_you = models.TextField()
    phone = models.IntegerField()
    upload_resume=models.FileField(upload_to='media')
    
    def __str__(self):
       return self.vacancy

class Rejected(models.Model):
    applicants = models.ForeignKey(Application,on_delete=models.CASCADE)
    
class Accepted(models.Model):
    applicants = models.ForeignKey(Application,on_delete=models.CASCADE)

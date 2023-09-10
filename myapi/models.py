from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    user_name=models.CharField(max_length=20)
    total=models.IntegerField(blank=True,null=True)
    today=models.IntegerField(default=0)
    totalweek=models.IntegerField(default=0)
    week=models.IntegerField(default=0)
    def __str__(self):
        return self.user_name
    

class dsa(models.Model):
    weekno = models.IntegerField(primary_key=True)
    topic=models.CharField(max_length=30)
    q1=models.URLField(max_length=50)
    q2=models.URLField(max_length=50)
    q3=models.URLField(max_length=50)
    q4=models.URLField(max_length=50)
    q5=models.URLField(max_length=50)

    def __str__(self):
        return "Week " + str(self.weekno)

class visits(models.Model):
    no=models.IntegerField(default=0)

from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    email= models.CharField(max_length=30,blank=True,null=True)
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
    d1=models.DateField(blank=True,null=True)    
    d2=models.DateField(blank=True,null=True)
    d3=models.DateField(blank=True,null=True)
    d4=models.DateField(blank=True,null=True)
    d5=models.DateField(blank=True,null=True)
    q1=models.URLField(max_length=50,blank=True,null=True)
    q2=models.URLField(max_length=50,blank=True,null=True)
    q3=models.URLField(max_length=50,blank=True,null=True)
    q4=models.URLField(max_length=50,blank=True,null=True)
    q5=models.URLField(max_length=50,blank=True,null=True)
    r1=models.URLField(max_length=30,blank=True,null=True)
    r2=models.URLField(max_length=30,blank=True,null=True)
    r3=models.URLField(max_length=30,blank=True,null=True)
    r4=models.URLField(max_length=30,blank=True,null=True)
    r5=models.URLField(max_length=30,blank=True,null=True)

    def __str__(self):
        return "Week " + str(self.weekno)

class visits(models.Model):
    no=models.IntegerField(default=0)

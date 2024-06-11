from django.db import models
from django.contrib.auth.models import User
import datetime
    
class SignIn(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    username=models.CharField(max_length=50,default='a')
    def __str__(self):
        return self.name
class handleProfileDetail(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    PRIVACY_CHOICES = [
        ('public', 'public'),
        ('private', 'private'),
    ]
    # connect two table Users table and handleProfileDetail table by foreign key
    # in which username will be same
    linked=models.ForeignKey(User,on_delete=models.CASCADE) 
    name=models.CharField(max_length=50,default='a')
    username=models.CharField(max_length=50,default='a')
    bio=models.TextField(default='a')
    gender=models.ImageField(max_length=10,choices= GENDER_CHOICES,default='female')
    privacy=models.ImageField(max_length=10,choices=PRIVACY_CHOICES,default='private')
    image=models.ImageField(upload_to='static/images',null=True)
    def __str__(self):
        return self.name
    
class userProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='static/images')
    
class storydata(models.Model):
    image=models.ImageField(upload_to='static/images')
    txt_stry=models.TextField()
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.username.username

class messegedata(models.Model):
    sent_by=models.CharField(max_length=20)
    sent_to=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    msg=models.TextField(max_length=100)
    timing=models.DateTimeField(null=True)
    def __str__(self):
        return self.sent_by

class postdata(models.Model):
    # postId=models.IntegerField(max_length=20)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post=models.ImageField(upload_to='static/images')
    caption=models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username.username

# SHOP PAGE
class brand(models.Model):
    name=models.CharField(max_length=100)

    def _str_(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=100)
    def _str_(self):
        return self.name
    

class product(models.Model):
    size_CHOICES = (
        ("sm", "small"),
        ("lg", "large"),
        ("md", "Medium"),
        ("XL", "Extra Large"),
        )

    size = models.CharField(max_length=9,choices=size_CHOICES,default="sm")
    title=models.TextField()
    rating=models.CharField(max_length=50)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='static/product_img',null=True)
    def _str_(self):
        return self.title
    
class likes(models.Model):
    likesCount=models.IntegerField()
    postId=models.IntegerField()
    likeDoneById=models.IntegerField()
    name=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
class comments(models.Model):
    commentsVal=models.CharField(max_length=100)
    postId=models.IntegerField()
    commentDoneById=models.IntegerField()

class company(models.Model):
    companyname=models.CharField(max_length=100)
    address=models.CharField( max_length=100)
    city=models.CharField( max_length=100)
    pincode=models.IntegerField()
    mobileno=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    companylogo=models.ImageField(upload_to='static/images')
    created_at=models.DateTimeField(default=datetime.datetime.now)

class job(models.Model):
    
    jobchoice = (
        ("internship", "internship"),
        ("fulltime", "fulltime"),
        ("fresher", "fresher"),
        )
    company=models.ForeignKey(company,on_delete=models.CASCADE)
    salary=models.IntegerField()
    skillsrequired=models.CharField(max_length=100)
    jobrequired=models.CharField(max_length=100)
    educationrequired=models.CharField( max_length=100)
    jobtype=models.CharField( max_length=100,choices=jobchoice)
    shift=models.CharField( max_length=100)
    weeksdays=models.CharField( max_length=100)
    description=models.TextField(max_length=100)
    rolesandresponsibility=models.TextField( max_length=100)
    created_at=models.DateTimeField(default=datetime.datetime.now)

class appliedJob(models.Model):
    job=models.ForeignKey(job,on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    applied_at=models.DateTimeField(auto_now=True)
    cv=models.FileField(upload_to='static/cv')
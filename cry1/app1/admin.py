from django.contrib import admin
from .models import SignIn ,handleProfileDetail,storydata,messegedata,brand
from .models import postdata,category,product,userProfile,likes,comments,company,job,appliedJob
admin.site.register(handleProfileDetail)
admin.site.register(SignIn)
admin.site.register(storydata)
admin.site.register(messegedata)
admin.site.register(postdata)
admin.site.register(category)
admin.site.register(product)
admin.site.register(brand)
admin.site.register(userProfile)
admin.site.register(likes)
admin.site.register(comments)
admin.site.register(company)
admin.site.register(job)
admin.site.register(appliedJob)
# Register your models here.

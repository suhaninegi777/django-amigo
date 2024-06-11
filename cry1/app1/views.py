from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SignIn,handleProfileDetail,product,userProfile
from .models import storydata,messegedata,postdata,likes,comments,company,job,appliedJob
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
from django.contrib.auth import hashers
from django.utils import timezone
import os
import datetime 
from datetime import datetime 
import json
import pyjokes
from django.http import JsonResponse


def c1(request):
    d={'a':'ankush'}
    jokes=pyjokes.get_joke()
    alluserpost=postdata.objects.all()
    # .values('username').distinct()
    allstories=storydata.objects.all().values('username').distinct()
    print('kaaaaaaaaaaaaa',allstories)
    k=[]
    for i in allstories:
        print(i)
        # wo id ko poora dictionary se compare karega or esa possible nahi to usse bhi value hi dena to i['username'] foreignkey he
        # yani integer value hi to wo compare ho jayega
        k.append(User.objects.get(id=i['username']))
    print(k)
    # for i in k:
    #     print(i.id)

    userimg=handleProfileDetail.objects.all()
    image_urls = []  # List to store image URLs
    for post in alluserpost:
        post.like_count = likes.objects.filter(postId=post.id).count()
        if likes.objects.filter(postId=post.id,likeDoneById=request.user.id).count()>0:
            post.has_liked=True
        else:
            post.has_liked=False

    if alluserpost is not None:
        
        for i in alluserpost:
            # print(i.username.get_profile().pic)
            i.post=os.path.basename(i.post.url)

    if userimg is not None:
        for im in userimg:
            # print(i.username.get_profile().pic)
            if im.image:
                print(im.image)
                im.image=os.path.basename(im.image.url)
    return render(request,"home.html",{'data':d,'jokes':jokes,'postdata':alluserpost,'storiesdata':k,'userimg':userimg})


def SignLogIn(request):
    return render(request,"SignLogIn.html")

def product_details(request,pname,pid):
    prod=product.objects.get(id=pid)
    return render(request,'singleproduct.html',{'prod':prod})

def Product(request):
    prods=product.objects.all()
    return render(request,'Product.html',{'prods':prods})

def sideNav(request):
    return render(request,"sideNav.html")


def recruit_form(request):
    return render(request,"recruit_form.html")

def candidateform(request):
    return render(request,"candidate_form.html")
    
def signin(request):
    if request.method=="POST":
        print(request.POST.get
              ('email'),request.POST.get
              ('password'),request.POST.get
              ('username'))
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # hashers a liabrary to encrypt the password
        password=hashers.make_password(password)
        username=request.POST.get('username')
        u=User.objects.create(username=username,first_name=name,email=email,password=password)
        print('hello',request.user)
        handleProfileDetail.objects.create(linked=u,name=name,username=username)
        print("user create")
        return render(request,"SignLogIn.html")
        # return render(request,"profile.html",{'username':username,'name':name})
    return render(request,"SignLogIn.html")

def mylogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("login time =>",username,password)
        userOB=authenticate(username=username,password=password)
        # users=SignIn.objects.filter(email=email,password=password)
        print("authenticate fn=>",userOB)
        print("request.user1",request.user)
        
        if userOB is not None:
            login(request,userOB)
            print("request.user2",request.user)
            return redirect('profile')
    return render(request,"SignLogIn.html")

def Storylejana(request):
    if request.method == 'POST':
        # request.FILES will only contain data if the request method was POST and the <form> that posted the
        # request has the attribute enctype="multipart/form-data". Otherwise, request.FILES will be empty.
        Stxt=request.POST.get('datagoing_text')
        print(Stxt)
        Surl = request.FILES['datagoing_url']
        print(Surl)
        username=request.user
        if Surl | Stxt is not None :
            print('start to huwa')
            storydata.objects.create(username=username,image=Surl,txt_stry=Surl)
            print("story lag gayi image wali")  
            return HttpResponse('Done')
            
        # elif(Stxt is not None):
        #     p=storydata.objects.create(username=username,txt_stry=Surl)
        #     print("story lag gayi text wali")   
            
        else:
            print('story nahi lagi')  
            return redirect('story')

        return redirect('profile')
    return render(request,"stories.html")

def storyShow(request):
    print('atlllllllllllleeeeeeeeeeeeeeeeeeaaaaaaaaaaasssssssssssssst',request.user)
    # Retrieve data from the request parameters
    data_id = request.GET.get('id')
    data_name = request.GET.get('name')
    print("ammmmmmmmmmmma",data_id)
    # data = storydata.objects.filter(id=data_id)  # Get all storydata objects for the current user
    data = storydata.objects.filter(username=data_id)  # Get all storydata objects for the current user
    print('daaaaaaaaaaaaaaaaaaaata',data)
    image_urls = []  # List to store image URLs
    if data:
        image_urls = [obj.image.url for obj in data]
        return JsonResponse({'image_urls': image_urls})
        #return HttpResponse(json.dumps({'stry':data}),content_type="application/json")
        
        # return render(request, "storyShow.html", {'image_urls': image_urls})
    else:
        return redirect('home')
    
    
def check_msgs(request,sent_idS): #sent_idS its a 2nd user
    
    sent_msgs=messegedata.objects.filter(sent_by=request.user,sent_to=User.objects.get(username=sent_idS)).order_by('timing')
    rev_msgs=messegedata.objects.filter(sent_by=sent_idS,sent_to=request.user).order_by('timing')
    # acha tarika he
    allmsg=[]
    sortedMsg=[]  
    
    print('sent msg ' + str(request.user) + ' ',sent_msgs)
    print('receive msg ' + str(sent_idS) + ' ',rev_msgs)
    for i in sent_msgs:
        msg=i.msg
        s_t=(f'{i.timing}')
        sd={'timing':s_t,
           'type':'sendBy',
           'msg':msg
        }
        allmsg.append(sd)
    for j in rev_msgs:
        msg=j.msg
        r_t=(f'{j.timing}')
        rd={'timing':r_t,
           'type':'receiver',
           'msg':msg
        }
        allmsg.append(rd)
    
    import pandas as pd
    df=pd.DataFrame(allmsg)
    # print(df)
    
    data=df.sort_values(by=['timing'])
    for index, row in data.iterrows():
        print(data.loc[index,'timing'])
        sortedMsg.append({
            'timing':data.loc[index,'timing'],
           'type':data.loc[index,'type'],
           'msg':data.loc[index,'msg']
        })
        # for i in len(sortedMsg):
        #    datetime_str= sortedMsg[i]['timing']
        # #    datetime_str = [ sub['timing'] for sub in sortedMsg ]
        #    datetime_obj = datetime.strptime(datetime_str,"%d%b%Y%H%M%S") 
        #    print(datetime_obj)
        #    sortedMsg[i]['timing'] = datetime_obj.s trftime("%H:%M")
    # print(data)
    print('all sent msges',sortedMsg)
    return HttpResponse(json.dumps({'msgs':sortedMsg}),content_type="application/json")

def messenger(request):
    us=''
    # user khud show nahi hoga messenger me
    # if request.user!=User:
    us=User.objects.all().exclude(username=request.user)
         
    if request.method == 'POST':
        msg=request.POST.get('msg_typing')
        sent_to=User.objects.get(username=request.POST.get('uid'))
        sent_by=request.user
        timing=timezone.now()
        messegedata.objects.create(sent_to=sent_to,sent_by=sent_by,msg=msg,timing=timing)
        return HttpResponse('Done')
        # user_data=messegedata.objects.filter(sent_by=request.user)
        # # important-> print(user_data[0].msg,type(user_data[0].sent_by),type(str(request.user)))
        
        # # for i in us:
        # #     i.image=os.path.basename(i.image.url)
        # # print(us)
        # if(user_data[0].sent_by==str(request.user)): #samne wale user ke liye kya condition hogi idk
        #     return render(request,'messenger.html',{'mera_msg':user_data,'alluser':us})
        
        # return render(request,'messenger.html',{'mera_msg':user_data,'alluser':us})
    
    # msgOB=messegedata.objects.get()
    return render(request,'messenger.html',{'alluser':us})


def save_prof_details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        # username=request.POST.get('username')
        gender=request.POST.get('gender')
        privacy=request.POST.get('privacy')
        bio=request.POST.get('bio')
        image=request.FILES['image']
        print("hello",request.user)
    #   sir se pooxna he ye
        # if image==null:
        #     image=
        # handleProfileDetail.objects.create(bio=bio,image=image,name=name,gender=gender,privacy=privacy).save()
        data=handleProfileDetail.objects.get(linked=request.user)
        print("data",data)
        data.bio=bio
        data.image=image
        data.gender=gender
        data.privacy=privacy
        data.save()
        data1= User.objects.get(username=request.user)
        data1.first_name=name
        data1.save()
        
        print("handleProfileDetail=>",request.user)
        pd=postdata.objects.filter(username=request.user)
        # for i in pd:
        #     i.post=os.path.basename(i.post.url)
        # data=handleProfileDetail.objects.filter(username=username)
        
        if data:
            return render(request,"profile.html",{
                "username":data.username,
                "bio":data.bio,
                "name":data1.first_name,
                "gender":data.gender,
                "image":data.image.url,
                "privacy":data.privacy,
                "pd":pd
                })
        else:
            print("nothing")
    return render(request,"profile.html",)


def prof(request):
    username=request.user
    
    if request.method=='POST':
        print('pls yaha tk to aaja')
        adpost=request.FILES['adpost']
        caption=request.POST.get('caption')
        print("ho kyu nahi raha she ",adpost,caption)
        postdata.objects.create(username=request.user,caption=caption,post=adpost)
   
    pd=postdata.objects.filter(username=request.user)
    data=handleProfileDetail.objects.get(linked=request.user)
    data1= User.objects.get(username=request.user)
    
    # for i in pd:
    #     i.post=os.path.basename(i.post.url)
    return render(request,"profile.html",{
                'pd':pd , 
                "username":data.username,
                "bio":data.bio,
                "name":data1.first_name,
                "gender":data.gender,
                "image":data.image.url,
                "privacy":data.privacy,
                })
            
        # for i in pd:
            # i.post=os.path.basename(i.post.url)
        # return render(request,"profile.html",{'pd':pd})
def postthing(request,id):
    return render(request,"profile.html")
    
        
def SecUserProfile(request):
    return render(request,'SecUserProfile.html')

def searchpage(request):
    return render(request,'search.html')

def search(request,uname):
    a=User.objects.filter(username=uname)[0]
    print(a)
    pd=postdata.objects.filter(username=a)
    secusername=''
    for i in pd:
        secusername=i.username
        i.post=os.path.basename(i.post.url)
    return render(request,"SecUserProfile.html",{'pd':pd ,'username':secusername})
        # {'filtreddata':filtreddata}
    # return render(request,'search.html')

    
def viewsearch(request):
    searchdata = request.GET.get('searchdata')
    filtreddata=User.objects.filter(username__icontains=searchdata)
    print(filtreddata) 
    res=[]
    for i in filtreddata:
        res.append(
            {
                'url':f'/searchres/{i.username}',
                'uname':i.username
            }
        )
    print(res)
    return HttpResponse(json.dumps({'res':res}),content_type="application/json")

def like(request):
    # if request.method=='POST':
    lcount=request.GET.get('lcount')
    print("lcount",lcount)
    postid=request.GET.get('postid')
    print("post_id",postid)
    uname=request.GET.get('uname')
    print("whose post is this ->",uname)
    likes.objects.create(likesCount=lcount,postId=postid,likeDoneById=request.user.id)
    lik=likes.objects.filter(postId=postid).count()
    # tcount=len(lik)
#    l=likes.objects.filter(=id)
    return HttpResponse(lik)

def dislike(request):
    # if request.method=='POST':
    postid=request.GET.get('postid')
    print("post_id",postid)
    uname=request.GET.get('uname')
    print("whose post is this ->",uname)
    l=likes.objects.get(postId=postid,likeDoneById=request.user.id)
    l.delete()

    lik=likes.objects.filter(postId=postid).count()
    # tcount=len(lik)
#    l=likes.objects.filter(=id)
    return HttpResponse(lik)

def comment(request):
    if request.method=='POST':
        comVal=request.POST.get('comtVal')
        print('comVal',comVal)
        postid=request.POST.get('postid')
        print("whose post is this ->",postid)
        comments.objects.create(commentsVal=comVal,postId=postid,commentDoneById=request.user.id)
        #    c=comments.objects.get(comId=id)
        #    comshow=c.comVal
        #    return HttpResponse(json.dumps({'comshow':comshow}),content_type="application/json")
        return HttpResponse('done')
    pid=request.GET.get('pid')
    coms=comments.objects.filter(postId=pid)
    comsdata=[]
    for i in coms:
        comsdata.append({
            "Name":User.objects.get(id=i.commentDoneById).username,
            "Comment":i.commentsVal
        })
    print(comsdata)
    return HttpResponse(json.dumps({'data':comsdata}), content_type="application/json")


def addcompany(request):
    if request.method=='POST':
        companyname=request.POST.get('Company_name')
        address=request.POST.get('enter_address')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        mobileno=request.POST.get('mbno')
        user=request.user
        companylogo=request.FILES['logo']

        comOB=company()
        comOB.companyname=companyname
        comOB.address=address
        comOB.city=city
        comOB.pincode=pincode
        comOB.mobileno=mobileno
        comOB.user=user
        comOB.companylogo=companylogo
        comOB.save()
        return redirect('jobs')

    return render(request,'addcompany.html')



def addjob(request):

    if request.method=='POST':
        companynamne=company.objects.get(id=request.POST.get('cid'))
        salary=request.POST.get('Salary')
        skillsrequired=request.POST.get('skills')
        jobrequired=request.POST.get('job_required')
        educationrequired=request.POST.get('education_required')
        jobtype=request.POST.get('job_type')
        shift=request.POST.get('shift')
        weeksdays=request.POST.get('weekDays')
        description=request.POST.get('Description')
        rolesandresponsibility=request.POST.get('Roles_Responsibilty')


        jobOB=job()
        jobOB.company=companynamne
        jobOB.salary=salary
        jobOB.skillsrequired=skillsrequired
        jobOB.jobrequired=jobrequired
        jobOB.educationrequired=educationrequired
        jobOB.jobtype=jobtype
        jobOB.shift=shift
        jobOB.weeksdays=weeksdays
        jobOB.description=description
        jobOB.rolesandresponsibility=rolesandresponsibility

        jobOB.save()
        
        return redirect('jobs')
    compDATA=company.objects.filter(user=request.user)
    return render(request,'recruit_form.html',{'com':compDATA})



def jobs(request):
    jobdata=job.objects.all().order_by('-created_at')

    return render(request,'job_portal.html',{'jobs':jobdata})

def myjobs(request):
    # com=company.objects.get(user=request.user)
    jobdata=job.objects.all().order_by('-created_at')
    data=[]
    for j in jobdata:
        if j.company.user==request.user:
            aplicants=appliedJob.objects.filter(job=j)
            data.append({
                'job':j,
                'aplicants':aplicants
            })
    
    applieddata=appliedJob.objects.filter(applicant=request.user)
    return render(request,'myjobs.html',{'data':data,'applieddata':applieddata})


def applyjob(request):
    if request.method=='POST':
        aplicant=request.user
        jobid=job.objects.get(id=request.POST.get('jid'))
        cv=request.FILES['cv']
        print(cv)
        if aplicant != jobid.company.user:
            appliedJob.objects.create(applicant=aplicant,job=jobid,cv=cv)
            return redirect('jobs')
        else:
            return redirect('jobs')
        
    return redirect('jobs')






    # global una
       
    # try:
    #     if una != sent_idS:
    #         print('write now seconduser',sent_idS)
    #         print('before seconduser',una) 
    #         una
    #         una=sent_idS
    #     # Do something
    # except NameError:
        
    #     una=sent_idS
    #     print("2user is asigned to una ")
        
           
# for i in sent_msgs:
#         for j in rev_msgs:
#             if s_t<r_t:
#                 print('receive tining is jada and send timing kam' +s_t+"sent timing" +r_t+"receive itming" )
                
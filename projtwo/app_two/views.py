from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Logininfo
from .forms import formName,userinfoform,userprofileinfoform
#### for direct login throgh webpage!!!!
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse('Go to /user/ to check info Go to formpage to signup!!')

@login_required
def special(request):
    return HttpResponse('you are logged in')

@login_required
def user_logout(request):
    logout(request)
    return redirect('app_two:userinfo')


def userinfo(request):
    record_list=Logininfo.objects.order_by('first_name')
    detail_dict={'records':record_list}
    return render(request,'app_two/index.html',context=detail_dict)
def forminfo(request):
    info=formName()
    if request.method=='POST':
        info=formName(request.POST)
        if info.is_valid():
            print('SUccess')
            info.save()
            #return index(request)
            # print('NAME:'+info.cleaned_data['name'])
            # print('Email: '+info.cleaned_data['email'])
            # print('TEXT:'+info.cleaned_data['text'])
    return render(request,'app_two/forms.html',{'info':info})

#Authentcation...
def register(request):
    registered=False
    if request.method=='POST':
        user_info=userinfoform(data=request.POST)
        profile=userprofileinfoform(data=request.POST)
        if user_info.is_valid() and profile.is_valid():
            user=user_info.save()
            user.set_password(user.password)
            user.save()
            print('********')
            print(user.username)
            print('*********')

            prof=profile.save(commit=False)
            prof.user=user
            print('11111')
            print(prof.user)

            if 'profile_pics' in request.FILES:
                prof.profile_pic=request.FILES['profile_pics']
            
            prof.save()

            registered=True

        else:
            print(user_info.errors,profile.errors)
    else:
        user_info=userinfoform()
        profile=userprofileinfoform()

    return render(request,'app_two/registeration.html',
    {'user_info':user_info,
    'profile':profile,
    'registered':registered})



def user_login(request):
    if request.method=='POST':
        #username=request.POST.get('username')
        testcase=request.POST.get('testcase')
        password=request.POST.get('password')
        print(testcase)

        user=authenticate(username=testcase,password=password)
        if user:
            print('yahpooo')
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app_two:index'))
            else:
                return HttpResponse('ACCOUNT NOT SIGNED UP')
        else:
            print('invalid entry tried!!')
            print('username:{} password:{}'.format(testcase,password))
            return HttpResponse('invalid login')
    else:
        return render(request,'app_two/login.html')

    
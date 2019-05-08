from django.shortcuts import render, redirect
from django.contrib import  messages, auth
from django.contrib.auth.models import User
from Student.models import Student
# Create your views here.



def login(request):
    global user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(username=username,password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            send_dict = {
            'user': user,
            }
            messages.success(request, 'You are now logged in')
            return redirect('dashboard_'+str(user))

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard_17103036(request):
#    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
#    print(user_contacts)
    global user
    queryset_list = Student.objects.get(sid = int(str(user)))
    #print(queryset_list.city)
    #queryset_list = queryset_list.filter(sid__iexact=user)
    print(queryset_list)
    context={
        'user':queryset_list,
    }
    return render(request,'accounts/dashboard_17103036.html',context)

def dashboard_17103042(request):
#    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
#    print(user_contacts)
    global user
    queryset_list = Student.objects.get(sid = int(str(user)))
    #print(queryset_list.city)
    #queryset_list = queryset_list.filter(sid__iexact=user)
    print(queryset_list)
    context={
        'user':queryset_list,
    }
    return render(request,'accounts/dashboard_17103042.html',context)

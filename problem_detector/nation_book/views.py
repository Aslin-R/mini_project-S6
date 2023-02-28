from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import ProblemStatements
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):

    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)

                user.save()
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect('register')

        print(username,email,password)
        return redirect('index')

    else:
        return render(request,'register.html')

def login(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        elif user is None:
            messages.info(request,'Fill the Form !')
            return redirect('login')
        else:
            messages.info(request,'invalid data')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def about_us(request):
    return render(request,'about.html')

def problem_statements(request):
    
    problems_statement=ProblemStatements()
    problems_statement.statement_name="Drugs"
    problems_statement.statement_id=1
    problems_statement.statement_desc='Major problem'
    
    return render(request,'problem-statements.html',{'problem_statement':problems_statement})


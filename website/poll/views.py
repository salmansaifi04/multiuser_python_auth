from django.shortcuts import render
from .models import Student, Teacher
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from .forms import StudentSignUpForm, TeacherSignUpForm, LoginForm,EditTeacherProfile, EditStudentProfile
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'poll/home.html')

def register(request):
    return render(request, 'poll/register.html')

### student registration View ###
def stureg(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = StudentSignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Register !!! now you can login !!!')
        else:
            fm = StudentSignUpForm()
        return render(request, 'poll/stu_reg.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


### Tecaher registration view ###

def teacher_reg(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = TeacherSignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully login !!! now you can login !!!')

        else:
            fm = TeacherSignUpForm()
        return render(request, 'poll/teacher_reg.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


### login ###
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    messages.success(request, 'login successfully')
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = LoginForm()
        return render(request, 'poll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

### profile ###
def profile(request):
    if request.user.is_authenticated:
        if request.user.is_student == True:
            fma = Student.objects.get(user__username=request.user)
            fm = EditStudentProfile(instance=fma)
        elif request.user.is_teacher == True:
            fma = Teacher.objects.get(user__username=request.user)
            fm = EditTeacherProfile(instance=fma)
        else:
            return HttpResponse('''Plz login as a teacher and student!!!<a href="/">Home</a>''')
        return render(request, 'poll/profile.html', {'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')

### logout ###
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django import forms
from django.db import transaction
from django.utils.translation import gettext, gettext_lazy as _
from .models import CLASS_SECTION, CLASS_STANDARD, STREAM, User, Student, Teacher


### student registration form ###
class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    standard = forms.CharField(widget=forms.Select(choices=CLASS_STANDARD,attrs={'class': 'form-control'}))
    class_section = forms.CharField(required=True,widget=forms.Select(choices=CLASS_SECTION , attrs={'class': 'form-control'}))
    stream = forms.CharField(widget=forms.Select(choices=STREAM, attrs={'class': 'form-control'}))
    roll_no = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        widgets ={
            'username' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
        fields = [ 'username' ,'first_name', 'last_name', 'standard', 'class_section', 'stream', 'roll_no']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.standard = self.cleaned_data.get('standard')
        student.class_section = self.cleaned_data.get('class_section')
        student.stream = self.cleaned_data.get('stream')
        student.roll_no = self.cleaned_data.get('roll_no')
        student.save()
        return user



### teacher registration form ###
class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    classes_taught = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        widgets ={
            'username' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
        fields = [ 'username' ,'first_name', 'last_name', 'subject', 'classes_taught', 'number']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.subject = self.cleaned_data.get('subject')
        teacher.classes_taught = self.cleaned_data.get('classes_taught')
        teacher.number = self.cleaned_data.get('number')
        teacher.save()
        return user

### login form ###
class LoginForm(AuthenticationForm):
    username = UsernameField(required=True,label='username', widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(required=True,label =_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class EditTeacherProfile(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = Teacher
        widgets ={
            'user' : forms.TextInput(attrs={'readonly':True}),
            'subject' : forms.TextInput(attrs={'readonly':True}),
            'classes_taught' : forms.TextInput(attrs={'readonly':True}),
            'number' : forms.TextInput(attrs={'readonly':True}),
            
            
        }
        fields =  ('user', 'subject', 'classes_taught', 'number')
    labels = {'user':'user_id'}        

class EditStudentProfile(UserChangeForm):
    password = None
    class Meta:
        model = Student
        widgets ={
            'user' : forms.TextInput(attrs={'readonly':True}),
            'standard' : forms.TextInput(attrs={'readonly':True}),
            'class_section' : forms.TextInput(attrs={'readonly':True}),
            'stream' : forms.TextInput(attrs={'readonly':True}),
            'rollno' : forms.TextInput(attrs={'readonly':True}),
            
        }
        fields = [ 'user' ,'standard', 'class_section', 'stream', 'roll_no']
        labels = {'user':'user_id'}        
        

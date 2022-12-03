from cProfile import label
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Nacos_ID, Student, Student_Level, Student_Semester, Transaction, User, Student_Session

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['app_no', 'username', 'email', 'password1', 'password2']
        widgets = {
            'app_no' : forms.TextInput(attrs={'class': 'form-control'}),
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password1' : forms.TextInput(attrs={'class': 'form-control'}),
            'new_password2' : forms.TextInput(attrs={'class': 'form-control'}),
        }



class UserImage(ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
        widgets = {
            'avatar' : forms.FileInput(attrs={'id': 'passport'}),
        }

class RegnoForm(ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no']
        widgets = {
            'reg_no' : forms.TextInput(attrs={'id': 'reg_no', 'class': 'form-control'}),
        }


class StudentSessionForm(ModelForm):
    class Meta:
        model = Student_Session
        fields = '__all__'
        exclude = ['app_no', 'status']
        widgets = {
            'session' : forms.Select(
                attrs={
                    'id': 'session', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
        }


class StudentLevelForm(ModelForm):
    class Meta:
        model = Student_Level
        fields = '__all__'
        exclude = ['app_no', 'status']
        widgets = {
            'level' : forms.Select(
                attrs={
                    'id': 'level', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
        }

class StudentSemesterForm(ModelForm):
    class Meta:
        model = Student_Semester
        fields = '__all__'
        exclude = ['app_no', 'status']
        widgets = {
            'semester' : forms.Select(
                attrs={
                    'id': 'semester', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
        }


class StudentIDForm(ModelForm):
    class Meta:
        model = Nacos_ID
        fields = '__all__'
        #exclude = ['app_no', 'status']
        widgets = {
            'level' : forms.Select(
                attrs={
                    'id': 'level', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
            'programme' : forms.Select(
                attrs={
                    'id': 'programme', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
            'session' : forms.Select(
                attrs={
                    'id': 'session', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
            'reg_no' : forms.TextInput(attrs={'class':'form-control'}),
            'fullname' : forms.TextInput(attrs={'class':'form-control'}),
            'passport' : forms.FileInput(attrs={'id': 'passport'}),
        }      


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['payment_ref', 'payment_status', 'payment_date', 'app_no']
        widgets = {
            'level' : forms.Select(
                attrs={
                    'id': 'level', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
            'payment_type' : forms.Select(
                attrs={
                    'id': 'payment_type', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                                
                    }),
            'session' : forms.Select(
                attrs={
                    'id': 'session', 
                    'class': 'ml-5 mdb-select dropdown-success darken-4 colorful-select initialized md-form',
                    
                    }),
            'app_no' : forms.TextInput(attrs={'class':'form-control'}),
            # '' : forms.TextInput(attrs={'class':'form-control'}),
            'payment_amount' : forms.NumberInput(attrs={'class':'form-control', 'id':'amount'}),
        }        
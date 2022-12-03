from distutils.command.upload import upload
import email
from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from django.utils.crypto import get_random_string

#when you want to customize your user Model import this
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class Student(models.Model):
    app_no = models.CharField("Application No",unique=True, null=False, primary_key=True, max_length=50)
    reg_no = models.CharField("Registration No", max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField("First Name", max_length=50)
    middle_name = models.CharField("Middle Name", max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    sex = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField("State of Origin", max_length=50)
    lga = models.CharField("Local Governmant",max_length=50)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    department = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)


    def __str__(self):
        return self.last_name +' '+ self.first_name +' '+ self.middle_name
    

class UserManager(BaseUserManager):
    def create_user(self, email,  password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)  # change password to hash
        user.save()
        return user
        
    def create_superuser(self, email,  password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField("Student Email", unique=True, null=True)
    app_no = models.CharField("Application No", unique=True, null=False, primary_key=True, max_length=50)
    avatar = models.ImageField("Profile Picture", null=True, upload_to="avatar/", default="avatar/man.png")

    # this part makes the user user to login using email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.app_no
    
    objects = UserManager()




class School_Session (models.Model):
    session = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.session

class Semester(models.Model):
    semester = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.semester

class Level(models.Model):
    level = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.level

class Programme(models.Model):
    programme = models.CharField(max_length=50)

    def __str__(self):
        return self.programme    

class Student_Level(models.Model):
    app_no = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level,  on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.level.level
    

class Student_Semester(models.Model):
    app_no = models.ForeignKey(User, on_delete=models.CASCADE)
    semester =models.ForeignKey(Semester,  on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.semester.semester
    


class Student_Session(models.Model):
    app_no = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(School_Session,  on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.session.session


class Nacos_ID(models.Model):
    reg_no = models.CharField("Reg No", unique=True, max_length=50)
    fullname = models.CharField("Student Name", max_length=100)
    session = models.ForeignKey(School_Session,  on_delete=models.SET_NULL, null=True, default='Select Session')
    level = models.ForeignKey(Level,  on_delete=models.SET_NULL, null=True, default='Select Level')
    programme =models.ForeignKey(Programme,  on_delete=models.SET_NULL, null=True, default='Select Programme')
    passport = models.ImageField("Passport", default="logo.png", null=True, upload_to='passports/', height_field=None, width_field=None, max_length=None)



class Payment_Type(models.Model):
    name = models.CharField("Payment Type", max_length=50, null=False)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    


class Transaction(models.Model):
    app_no = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_ref = models.CharField(max_length=50)
    payment_type = models.ForeignKey(Payment_Type, on_delete=models.SET_NULL, null=True, default='Payment Type' )
    payment_amount = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, default='Select Level')
    session = models.ForeignKey(School_Session, on_delete=models.SET_NULL, null=True, default='Select Session')
    payment_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    payment_status = models.BooleanField(default=False)


    class Meta:
        ordering = ('-payment_date',)

    def __str__(self):
        return self.payment_ref

    def save(self, *args, **kwargs):
        while not self.payment_ref:
            ref = get_random_string(length=12).upper()
            isexist_ref = Transaction.objects.filter(payment_ref=ref)

            if not isexist_ref:
                self.payment_ref = ref
        super().save(*args, **kwargs)

    




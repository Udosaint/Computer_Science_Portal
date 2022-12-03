from email import message
from gettext import install
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm

from .paystack import Paystack

from .models import Nacos_ID, Payment_Type, School_Session, Student_Level, Student_Semester, Student_Session, Transaction, User, Student
from .forms import ChangePasswordForm, RegnoForm, StudentCreationForm, StudentIDForm, StudentLevelForm, StudentSemesterForm, StudentSessionForm, TransactionForm, UserImage

from django.conf import settings

from django.utils.crypto import get_random_string
# Create your views here.

def Home(request):
    page = "Home"
    return render(request, 'index.html', {'page':page})

def About(request):
    page = "ABOUT"
    return render(request, 'about.html', {'page':page})

def Contact(request):
    page = "CONTACT"
    return render(request, 'contact.html', {'page':page})

def Announcement(request):
    page = "NEWS"
    return render(request, 'news.html', {'page':page})

def studentLogin(request):
    page = "LOGIN"
    

    if request.user.is_authenticated:
        return redirect('student-home')

    
    if request.method == "POST":
        message = None

        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            
        except:
            message = "Email not found"

        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('student-home')
        else:
            message = "Email or Password is not valid"
            return render(request, 'login.html', {'page':page, 'message':message})
        
    return render(request, 'login.html', {'page':page})


def studentRegister(request):
    page = "VALIDATE"

    if request.method == 'POST':
        app_no = request.POST.get('app_no').upper()
        studentApp_no = None

        try:
            
            studentApp_no = Student.objects.get(app_no=app_no)
        except:
            errors = "not found"

        if studentApp_no is not None:
            AppNo = studentApp_no.app_no
            form = StudentCreationForm(initial={'app_no':AppNo})
            page = "REGISTER"
            context = {'page':page, 'AppNo':AppNo, 'form':form}
            return render (request, 'register.html', context)
        else:
            message = "No Student with this Application Number"
            context = {'page':page, 'message':message, 'app_no':app_no}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {'page':page})    


def studentLogout(request):
    logout(request)
    return redirect('home')


def createStudent(request):

    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        app_no = request.POST.get('app_no')
        page = "REGISTER"
        print(app_no)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            page = "CONGRATULATIONS"
            context = {'page':page}
            return render (request, 'register.html', context)
        else:
            message = "An error Occured"
            context = {'page':page, 'message':message, 'app_no':app_no, 'form':form}
            return render (request, 'register.html', context) 

        #context = {'page':page, 'app_no':app_no, 'form':form} 
    return render (request, 'register.html', context)



@login_required(login_url='login')
def studentHome(request):
    user = request.user
    form = UserImage(instance=user)
    page = "Dashboard Student"
    app_no = request.user.app_no
    student = Student.objects.get(app_no=app_no)

    # current session
    session = Student_Session.objects.filter(status=True)
    level = Student_Level.objects.filter(status=True)
    semester = Student_Semester.objects.filter(status=True)

    if request.method == "POST":

        form = UserImage(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('student-home')

    context = {'page':page, 'student':student, 'form':form, 'session':session, 'level':level, 'semester':semester}
    return render(request, 'student/index.html', context)


#not using it for now
@login_required(login_url='login')
def studentImage(request):

    return render(request, 'student/index.html')


def studentID(request):
    student = Student.objects.get(app_no=request.user.app_no)
    nacosId = Nacos_ID.objects.filter(reg_no=student.reg_no)
    fullname = student.last_name + ' ' + student.first_name + ' ' + student.middle_name
    form = StudentIDForm(initial={'fullname':fullname, 'reg_no':student.reg_no})

    if request.method == "POST":

        form = StudentIDForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student-home')
        else:
            message = "An error Occured"
            return render(request, 'student/nacosid.html', {'message':message})

    context = {'form':form, 'student':student, 'nacosId':nacosId}
    return render(request, 'student/nacosid.html', context) 

def studentSession(request):
    page = "Session"
    form = StudentSessionForm()
    sessions = School_Session.objects.all()
    context = {'page':page, 'sessions':sessions, 'form':form}
    return render(request, 'student/updatesession.html', context) 

def updateSession(request):

    if request.method == "POST":
        form = StudentSessionForm(request.POST)

        # get select * from studentSession where appno = user and update the status to 0
        Student_Session.objects.filter(app_no=request.user).update(status=0)

        # insert the new session that is active
        if form.is_valid():
            session = form.save(commit=False)
            session.app_no = request.user
            session.save()
            return redirect('student-home')
    return render(request, 'student/updatesession.html')



def studentLevel(request):
    page = "Level"
    form = StudentLevelForm()
    levels = School_Session.objects.all()
    context = {'page':page, 'levels':levels, 'form':form}
    return render(request, 'student/updatesession.html', context) 
    
def updateLevel(request):
    page = "Level"
    if request.method == "POST":
        form = StudentLevelForm(request.POST)

        # get select * from studentSession where appno = user and update the status to 0
        Student_Level.objects.filter(app_no=request.user).update(status=0)

        # insert the new session that is active
        if form.is_valid():
            level = form.save(commit=False)
            level.app_no = request.user
            level.save()
            return redirect('student-home')
    return render(request, 'student/updatesession.html', context) 


def studentSemester(request):
    page = "Semester"
    form = StudentSemesterForm()
    semesters = School_Session.objects.all()
    context = {'page':page, 'semesters':semesters, 'form':form}
    return render(request, 'student/updatesession.html', context) 

def updateSemester(request):
    page = "Semester"
    if request.method == "POST":
        form = StudentSemesterForm(request.POST)

        # get select * from studentSession where appno = user and update the status to 0
        Student_Semester.objects.filter(app_no=request.user).update(status=0)

        # insert the new session that is active
        if form.is_valid():
            semester = form.save(commit=False)
            semester.app_no = request.user
            semester.save()
            return redirect('student-home')
    return render(request, 'student/updatesession.html') 

def updateRegno(request):
    page = "Update-Regno"
    form = RegnoForm()
    student = Student.objects.get(app_no=request.user)
    if request.method == "POST":
        form = RegnoForm(request.POST, instance=student)

        # get select * from studentSession where appno = user and update the status to 0
        #Student_Semester.objects.filter(app_no=request.user).update(status=0)

        # insert the new session that is active
        if form.is_valid():
            # semester = form.save(commit=False)
            # semester.app_no = request.user
            form.save()
            return redirect('student-home')

    return render(request, 'student/updateregno.html', {'form':form, 'student':student}) 


def studentPassword(request):
    student = Student.objects.get(app_no=request.user)
    form = ChangePasswordForm(user=request.user)

    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('student-home')
    return render(request, 'student/changepassword.html', {'student':student, 'form':form}) 



def studentPayment(request):
    page = "Payment Mode"
    student = Student.objects.get(app_no=request.user)

    form = TransactionForm()

    # checking if the request is get
    if request.method == "GET":

        # checking if the request is get with amount as the parameter
        if request.GET.get('amount'):
            payment_type_id = request.GET.get('amount')
            payment_type = Payment_Type.objects.get(pk=payment_type_id)
            payment_amount = payment_type.amount
            return HttpResponse(payment_amount)

    if request.method == "POST":


        page = "Proceed payment"
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.app_no = request.user
            #transaction.payment_ref = ref
            transaction.save()
            return render(request, 'student/nacosdue.html', {'page':page, 'student':student, 'transaction':transaction, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
        else:
            print ("error in the form")
            return render(request, 'student/nacosdue.html', {'page':page, 'student':student, 'form':form})

    return render(request, 'student/nacosdue.html', {'page':page, 'student':student, 'form':form}) 


def CancelPayment(request, ref):
    Transaction.objects.filter(payment_ref=ref).delete()
    return redirect('payments')

def VerifyPayment(request, ref):
    
    paystack = Paystack()
    verify_status = paystack.verrify_payment(ref)

    if verify_status is True:
        Transaction.objects.filter(payment_ref=ref).update(payment_status=1)
        return redirect('student-home')
    else:
        print("failed")
    return HttpResponse(verify_status)


def studentPaymentList(request):
    page = "Dashboard Student"
    student = Student.objects.get(app_no=request.user)
    transactions = Transaction.objects.filter(app_no=request.user)
    return render(request, 'student/paymentlist.html', {'page':page, 'student':student, 'transactions':transactions}) 

@login_required(login_url='login')
def studentPaymentReceipt(request, ref):
    if request.method == "GET":
        student = Student.objects.get(app_no=request.user)
        transaction = Transaction.objects.get(payment_ref=ref)
        print(transaction)
        return render(request, 'student/viewreceipt.html', {'transaction':transaction, 'student':student}) 

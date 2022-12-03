from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('news', views.Announcement, name='news'),

    path('login/', views.studentLogin, name='login'),
    path('register/', views.studentRegister, name='register'),
    path('logout/', views.studentLogout, name='logout'),
    path('create-student/', views.createStudent, name='create-student'),


    path('student/', views.studentHome, name='student-home'),
    # for uploading the student picture
    path('student/avatar', views.studentImage, name='student-avatar'),
    path('student/student-id/', views.studentID, name='student-id'),

    path('student/session/', views.studentSession, name='session'),
    path('student/update-session/', views.updateSession, name='update-session'),

    path('student/level/', views.studentLevel, name='level'),
    path('student/update-level/', views.updateLevel, name='update-level'),

    path('student/semester/', views.studentSemester, name='semester'),
    path('student/update-semester/', views.updateSemester, name='update-semester'),

    path('student/update-regno/', views.updateRegno, name='update-regno'),
    
    path('student/change-password/', views.studentPassword, name='change-password'),
    path('student/payments/', views.studentPayment, name='payments'),
    path('student/payment-list/', views.studentPaymentList, name='payment-list'),

    path('student/cancel-payment/<str:ref>/', views.CancelPayment, name='cancel-payment'),
    path('student/verify-payment/<str:ref>/', views.VerifyPayment, name='verify-payment'),
    path('student/payment-receipt/<str:ref>/', views.studentPaymentReceipt, name='payment-receipt'),

]

from django.contrib import admin

from .models import Nacos_ID, Programme, User, Student, School_Session, Semester, Level, Student_Session, Student_Level, Student_Semester, Payment_Type, Transaction
# Register your models here.

class StudentSessionAdmin(admin.ModelAdmin):
    list_display = ['app_no', 'session', 'status']

class StudentLevelnAdmin(admin.ModelAdmin):
    list_display = ['app_no', 'level', 'status']

class StudentSemesterAdmin(admin.ModelAdmin):
    list_display = ['app_no', 'semester', 'status']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['app_no', 'first_name', 'last_name', 'phone']


class NacosIDAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'fullname', 'session', 'programme']

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['app_no', 'payment_type', 'payment_ref', 'payment_amount', 'payment_status', 'payment_date']

admin.site.register(User)
admin.site.register(Student, StudentAdmin)

admin.site.register(School_Session)
admin.site.register(Semester)
admin.site.register(Level)

admin.site.register(Student_Session, StudentSessionAdmin)
admin.site.register(Student_Semester, StudentSemesterAdmin)
admin.site.register(Student_Level, StudentLevelnAdmin)

admin.site.register(Nacos_ID, NacosIDAdmin)
admin.site.register(Programme)

admin.site.register(Payment_Type, PaymentTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
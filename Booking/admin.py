from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','patient_id', 'doctor','treatment', 'gender','status', 'age', 'phone', 'email', 'address','note')
    search_fields = ('name', 'phone', 'email')

@admin.register(Login)
class LoginAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('username', 'password', 'type')
    search_fields = ('username', 'type')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('RoomNumber',)
    search_fields = ('RoomNumber',)

@admin.register(Admin)
class AdminAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Name', 'phone', 'email')
    search_fields = ('Name', 'phone', 'email')

@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'email_id', 'place', 'gender','Speciality','About','DOB','Image')
    search_fields = ('name', 'contact_no', 'email_id')

@admin.register(Therapy)
class TherapyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Therapy',)
    search_fields = ('Therapy',)

@admin.register(Therapist)
class TherapistAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact_no', 'email_id', 'place', 'gender', 'Room','Image')
    search_fields = ('name', 'contact_no', 'email_id')

@admin.register(booking)
class BookingAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('Doctor','status', 'patientid','treatment', 'reg_date', 'reg_time','about')
    search_fields = ('Doctor__name', 'patientid__name', 'reg_date')

@admin.register(Schedule)
class ScheduleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('patientid', 'status','Therapist', 'Therapy', 'Date', 'number_of_session', 'starting_Time', 'ending_Time')
    search_fields = ('patientid__name', 'Therapist__name', 'Therapy__Therapy', 'Date')
@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['Status', 'color']
@admin.register(Statusbooking)
class StatusbookingAdmin(admin.ModelAdmin):
    list_display = ['Status', 'color']
@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['Department', ]
@admin.register(Treatment)
class TreatmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['Treatment', 'Department']
@admin.register(SessionStatus)
class SessionStatusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['session_date','session_group', 'ending_Time','starting_Time','status','schedule','session_number']
# @admin.register(casesheet)
# class CaseSheetAdmin(admin.ModelAdmin):
#     list_display = (
#         'patientid', 'Followup', 'Proposedtreatmentplan', 'Treatment', 'Srothusinvolved', 'Dhathupredominence',
#         'Doshapredominence', 'Amanirama', 'Regularmedications', 'PastMedicalandsurgicalhistory', 'Historyofpresentingcomplaints',
#         'Presentingcomplaints', 'Menstrualhistory', 'Allergies', 'Sleep', 'Digestion', 'Clinicaldetails'
#     )
#     search_fields = (
#         'patientid__name', 'Followup', 'Proposedtreatmentplan', 'Treatment', 'Srothusinvolved', 'Dhathupredominence',
#         'Doshapredominence', 'Amanirama', 'Regularmedications', 'PastMedicalandsurgicalhistory', 'Historyofpresentingcomplaints',
#         'Presentingcomplaints', 'Menstrualhistory', 'Allergies', 'Sleep', 'Digestion', 'Clinicaldetails'
#     )
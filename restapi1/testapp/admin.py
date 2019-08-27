from django.contrib import admin
from testapp.models import Employee, Education

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['e_no' , 'e_name','e_sal','e_mobile','e_city']

class EducationAdmin(admin.ModelAdmin):
    list_display=['e_no', 'highest_qualification','temporary_address','permanent_address']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Education,EducationAdmin)

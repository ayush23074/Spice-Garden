from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Recipie)

admin.site.register(Department)
admin.site.register(Employee_ID)
admin.site.register(Employee)
admin.site.register(Activity)


class EmployeeRatingAdmin(admin.ModelAdmin):
    list_display = ('employee', 'activity', 'rating')
    list_filter = ('employee', 'activity', 'rating')
    search_fields = ('employee__employee_name', 'activity__activity')

    
admin.site.register(EmployeeRating, EmployeeRatingAdmin)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    receipe_name = models.CharField(max_length=100)
    receipe_Description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe_images/")

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class Employee_ID(models.Model):
    employee_id = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.employee_id 
    
    class Meta:
        ordering = ['employee_id']

class Activity(models.Model):
    activity = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.activity
    
    class Meta:
        ordering = ['activity']

class Employee(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.SET_NULL, null = True, blank = True)
    employee_id = models.ForeignKey(Employee_ID, related_name='employeeid', on_delete=models.SET_NULL, null = True, blank = True)
    employee_name = models.CharField(max_length=100)
    employee_dob = models.DateField()
    employee_email = models.EmailField(unique = True)
    employee_phone = models.CharField(max_length=100)
    employee_address = models.TextField()

    def __str__(self)-> str:
        return self.employee_name
    
    class Meta:
        ordering = ['employee_name']
        verbose_name = "Employee"

class EmployeeRating(models.Model):
    employee = models.ForeignKey(Employee, related_name = 'EmployeeRating' , on_delete = models.SET_NULL, null = True, blank = True)
    activity = models.ForeignKey(Activity , related_name = 'Activity' , on_delete= models.SET_NULL, null = True, blank = True   )
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.employee.employee_name} - {self.activity.activity} - {self.rating}"
    class Meta:
        unique_together = ['employee', 'activity']

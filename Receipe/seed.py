from faker import Faker
from .models import *
import random
fake = Faker()

def seed_db(n=10):
    try:
        for _ in range(n):
            department_obj = Department.objects.all()
            random_index =random.randint(0,len(department_obj)-1)
            department = department_obj[random_index]
            employee_id = Employee_ID.objects.create(employee_id=fake.unique.random_number(digits=3))
            Employee.objects.create(
                department=department,
                employee_id=employee_id,
                employee_name=fake.name(),
                employee_dob=fake.date_of_birth(),
                employee_email=fake.unique.email(),
                employee_phone=fake.phone_number(),
                employee_address=fake.address()
            )
    except Exception as e:
        print(e)

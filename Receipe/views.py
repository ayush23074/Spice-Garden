from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/Login/")
def receipe(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_Description = data.get("receipe_description")

        print(receipe_name, receipe_Description)
        print(receipe_image)

        
        Recipie.objects.create(
            receipe_name=receipe_name,
            receipe_Description=receipe_Description,
            receipe_image=receipe_image
        )

        return redirect("/Receipe/")
    return render(request, "Receipe.html", context={"page": "Receipe"})

@login_required(login_url="/Login/")
def update_receipe(request, id):
    queryset = Recipie.objects.get(id=id)

    if request.method =="POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_Description = data.get("receipe_description")

        queryset.receipe_name = receipe_name
        queryset.receipe_Description = receipe_Description
        if receipe_image:

            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect("/View_Receipe/")

    return render(request, "Update_Receipe.html", context={"page": "Update Receipe", "receipe": queryset})

@login_required(login_url="/Login/")
def View_receipe(request):
    queryset = Recipie.objects.all()
    
    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(receipe_name__icontains=search)

    return render(request, "View_Receipe.html", context={"page": "View Receipe", "receipe": queryset})

@login_required(login_url="/Login/")
def delete_receipe(request, id):
    Recipie.objects.filter(id=id).delete()
    return redirect("/Receipe/")

def Login_page(request):

    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
            return render(request, "Login.html", context={"page": "Login"})
        
        user = authenticate(username=username, password=password)

        if not user:
            messages.error(request, "Invalid password")
            return redirect("/Login/")
        
        else:
            login(request,user)
            return redirect("/Receipe/")
        
    return render(request, "Login.html", context={"page": "Login"})

def logout_page(request):
    logout(request)
    return redirect("/Login/")

def Register_page(request):

    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already taken")
            return render(request, "Register.html", context={"page": "Register"})


        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect("/Register/")
    

    return render(request, "Register.html", context={"page": "Register"})

from django.db.models import Q,Avg

def get_Employee(request):
    queryset = Employee.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        query = Q(employee_name__icontains=search) | \
            Q(department__department__icontains=search)
        if search.isdigit():
            query |= Q(employee_id=int(search))
        queryset = queryset.filter(query)

    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,"Ratings/Employee.html",context = {"page": "Employee Rating","queryset": page_obj})


def see_rating(request,id):
    employee = Employee.objects.filter(id =id)
    queryset = EmployeeRating.objects.filter(employee__id = id)
    overall_rating = queryset.aggregate(Avg("rating"))["rating__avg"]


    if request.method == "POST":
        data = request.POST
        activity = data.get("activity")
        rating = data.get("rating")

    return render(request , "Ratings/Employee_Rating.html", context = {"page": "Employee Rating","queryset": queryset, "overall_rating": overall_rating})
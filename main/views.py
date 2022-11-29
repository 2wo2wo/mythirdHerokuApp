from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Meal, Chair, Client
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import AddLogins, MealsForm
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect( reverse( "log-in"  ))
    return render(request , 'main/index.html',{
            "meals": Meal.objects.all()
        }) 

def just(request , just_id):
    chairs = Chair.objects.exclude(busy=True).all()
    return render(request, 'main/login.html',{
        "num":Meal.objects.get(pk = just_id),
        "chairs": chairs
    })  
@login_required
def book(request , name_meal):
    if request.method == "POST":        
        chair = Chair.objects.get(pk=int(request.POST["chair"]))
        chair.busy = True
        chair.save()
        meal = Meal.objects.get(pk=name_meal)
        client = Client.objects.get(User_id=request.user.id)
        client.meals.add(meal)
        client.chair.clear()
        client.chair.add(chair)
        return render(request, 'main/chair.html', {
            "chair_number": chair,
            "meal_name": meal
        })
    return render(request, 'main/error.html')

@login_required
def unbook(request , chair_id):
    if request.method == "POST": 
        chairs = Chair.objects.get(pk = int(chair_id))
        # make booked chairs by the user open         
        chairs.busy = False        
        chairs.save()
        client_chair = Client.objects.get(chair = chairs)
        client_chair.chair.clear()
        client_chair.meals.clear()
        return render(request, 'main/unbook.html' )
    return render(request, 'main/error.html' )


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["confirm-password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if password == password_confirm:
            user = User.objects.create_user(username, email , password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            copyUser = User.objects.get(username=username).id      
            form = AddLogins({
                "id":random.sample(range(100), 10),
                 "User_id": copyUser ,
                  "name": f"{first_name}  {last_name}"
                  })
            form.save()
            user = authenticate(request , username=username , password=password)
            login(request , user )
            return HttpResponseRedirect(reverse('index'))            
        else:
             return render(request , 'main/register.html' , {
                "message": "passwords do not match"
            })   
        
    return render(request , 'main/register.html')


@login_required
def povar(request):
    clients = Client.objects.exclude(meals=None).all()    
    return render(request , 'main/povar.html', {
        "clients":clients,
                    
    })    

def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request , 'main/log_in.html',{
                "message": "Invalid login or password"                
            }) 

    return render(request ,'main/log_in.html')       

@login_required
def logout_view(request):
    logout(request)
    return render(request , 'main/log_in.html' , {
        "message":"You logged out"
    })

@login_required
def addMeal(request):
    if request.method =="POST":
        meal_name = request.POST["meal"]
        price = float(request.POST["price"])
        info = request.POST["info"]
        form = MealsForm({
            "id": random.sample(range(100), 10),
            "name": meal_name,
            "price": price,
            "info" : info ,
        })
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('add'))
    meals=Meal.objects.all()
    return render(request , 'main/add_meal.html' ,{
        "meals":meals
    })
from django.shortcuts import render, redirect
from app0ne.models import TableOne
# Create your views here.
def home(request):
     if request.method == 'POST':
          name = request.POST.get('var_name')
          mobile = request.POST.get('mobile')
          email = request.POST.get('email')

          #print(f"Name: {name}, Mobile: {mobile}, Email: {email}")

          # Save data to the database
          TableOne.objects.create(name=name, mobile=mobile, email=email)
          return redirect("/")  # Redirect to the same page after saving data

     return render(request, 'home.html')


        

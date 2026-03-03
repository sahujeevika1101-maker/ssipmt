from django.shortcuts import render, redirect
from app0ne.models import TableOne
# Create your views here.
def home(request):
     user_data = TableOne.objects.all()  # Fetch all data from the database
     
     if request.method == 'POST':
          name = request.POST.get('var_name')
          mobile = request.POST.get('mobile')
          email = request.POST.get('email')
          file = request.FILES.get('file')  # Get the uploaded file

          #print(f"Name: {name}, Mobile: {mobile}, Email: {email}")

          # Save data to the database
          TableOne.objects.create(name=name, mobile=mobile, email=email, file=file)
          return redirect("/")  # Redirect to the same page after saving data
     #json
     data_front= {
          'data': user_data
     }
     return render(request, 'home.html',data_front)


        

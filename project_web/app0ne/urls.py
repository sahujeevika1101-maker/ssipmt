from django.urls import path
from app0ne.views import home

urlpatterns = [
    path('', home, name='home'),
] 
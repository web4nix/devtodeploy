from django.urls import path
from . import views
# bring in the views 
# create a method that is attached to view file

            

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'), 
    path('login', views.login, name='login'),  
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),   
]
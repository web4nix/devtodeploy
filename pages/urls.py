from django.urls import path
from . import views
# bring in the views 
# to create a method that is attached to view file

            

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
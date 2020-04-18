from django.urls import path
from . import views
# bring in the views 
# create a method that is attached to view file

            

urlpatterns = [
    path('', views.index, name='listings'),   # ''   goes to   /listings
    path('<int:listing_id', views.listing, name='listing'),   # goes to    /listings/123
    path('search', views.search, name='search'),
]
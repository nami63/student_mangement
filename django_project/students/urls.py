from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns for the students app as needed
]

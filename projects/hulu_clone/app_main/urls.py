from django.urls import path

from . import views

#APP NAME
app_name = 'name_of_app'

urlpatterns = [
    path('', views.index, name='my_index'),	   
]
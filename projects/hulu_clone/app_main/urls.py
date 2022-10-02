from django.urls import path

from . import views

#APP NAME
app_name = 'huclu'

urlpatterns = [
    path('', views.index, name='my_index'),	   
    path('login_signup', views.login_signup, name='login_signup'),	   
    path('login_signup_form', views.login_signup_form, name='login_signup_form'),   
    path('logout', views.logout, name='logout'),   
    path('dash', views.dash, name='dash'),   
]
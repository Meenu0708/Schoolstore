from .import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('courses', views.courses, name='courses'),
    path('courses/application', views.application, name='application'),
    path('logout', views.logout, name='logout'),


]

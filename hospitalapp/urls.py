
from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('form/', views.form, name='form'),
    path('appointments/', views.appointmentdetails, name='appointment'),
    path('users/', views.users, name='users'),
    path('products/', views.details, name='details'),
    path('adminhome/', views.adminhome, name='adminhome'),

]

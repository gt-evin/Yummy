
from django.contrib import admin
from django.urls import path
from anything import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register,name='register'),
    path('login/', views.login, name='login'),
    path('aptdetails/', views.appointmentdetails, name='details'),
    path('users/', views.users, name='users'),
    path('details/', views.details, name='details'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]



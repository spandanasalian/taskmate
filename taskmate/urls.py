
from django.contrib import admin
from django.urls import path, include
from todolist_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('todolist/',include('todolist_app.urls')),
    path('account/',include('users_app.urls')),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
   
]

from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Sahil Shrivastav"
admin.site.site_title = "Welcome to my dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
]
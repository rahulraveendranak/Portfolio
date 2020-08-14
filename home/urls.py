from django.contrib import admin
from django.urls import path
from home import views

#django admin header custamization
admin.site.site_header ="Developer Rahul"
admin.site.index_title ="Welcome"
admin.site.site_title = "Rahul's Dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'), 
]

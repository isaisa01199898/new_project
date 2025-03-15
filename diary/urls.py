from django.urls import path, include
from . import views

app_name='heart_libbot'
urlpatterns = [
        path('',views.index,name='index'),
]

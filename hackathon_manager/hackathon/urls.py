from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'hackathon'

urlpatterns = [
    path('', views.HackathonCreateView.as_view(), name="create"),
]

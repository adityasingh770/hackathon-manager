from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'hackathon'

urlpatterns = [
    path('', views.HackathonListView.as_view(), name="list"),
    path('create/', views.HackathonCreateView.as_view(), name="create"),
    path('update/<slug>', views.HackathonModifyView.as_view(), name="update"),
    path('detail/<slug>', views.HackathonDetailView.as_view(), name="detail"),
]

from django.urls import path
from . import views

app_name = 'hackathon'

urlpatterns = [
    path('', views.HackathonListView.as_view(), name="list"),
    path('create/', views.HackathonCreateView.as_view(), name="create"),
    path('update/<slug>', views.HackathonModifyView.as_view(), name="update"),
    path('detail/<slug>', views.HackathonDetailView.as_view(), name="detail"),
    path('delete/<slug>', views.HackathonDeleteView.as_view(), name='delete'),
    path('register/<slug>/', views.Register.as_view(), name="register"),
    path('unregister/<slug>/', views.Unregister.as_view(), name="unregister"),
    path('user_hackathons/', views.UserHackathonListView.as_view(),
         name="user_hackathons"),
    path('registered_user/', views.RegisteredUser.as_view(), name="registered"),
    path('unregistered_user/', views.UnregisteredUser.as_view(),
         name="not_registered"),
]

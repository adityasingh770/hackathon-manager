from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html",
         next_page=reverse_lazy('home')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]

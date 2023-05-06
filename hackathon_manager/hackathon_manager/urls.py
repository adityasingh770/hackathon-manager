from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('welcome/', views.WelcomePage.as_view(), name="welcome"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('about/', views.AboutPage.as_view(), name="about"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('hackathon/', include("hackathon.urls", namespace="hackathon")),
]

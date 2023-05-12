from django.urls import path
from . import views

app_name = 'submission'

urlpatterns = [
    path('', views.UserSubmissionListView.as_view(), name="list"),
    path('submit/<slug:hackathon_slug>/',
         views.SubmissionCreateView.as_view(), name="submit"),
    path('update/<pk>/',
         views.SubmissionUpdateView.as_view(), name="update"),
    path('detail/<pk>/',
         views.SubmissionDetailView.as_view(), name="detail"),
    path('delete/<pk>/',
         views.SubmissionDeleteView.as_view(), name="delete"),
]

from django.urls import path
import oauth2_provider.views as oauth2_views
from split import views

urlpatterns = [
    path('', views.root),
    path('register/', views.register),
    path('login/', oauth2_views.TokenView.as_view()),
    path('profile/', views.get_profile),
    path('add_friend/', views.add_friend),
]

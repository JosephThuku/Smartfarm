# users/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import CustomLoginView, FarmerSignUpView, GenerateFarmInsightsView, OpenAIChatView, login_view, signup_view, dashboard_view, farm_management_view

urlpatterns = [
    path('api/chat/', OpenAIChatView.as_view(), name='openai_chat'),

    path('', CustomLoginView.as_view(), name='login'),
    path('api/generate_farm_insights', GenerateFarmInsightsView.as_view(), name='generate_farm_insights'),


    path('login/', CustomLoginView.as_view(), name='login'),
    
    # path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('farm_management/', views.farm_management_view, name='farm_management'),
    path('signup/', FarmerSignUpView.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='farm:login'), name='logout'),
]

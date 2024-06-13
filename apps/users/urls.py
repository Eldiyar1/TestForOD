from django.urls import path

from apps.users import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('confirm/', views.VerifyOTP.as_view(), name='confirm'),
    path('login/', views.LoginView.as_view(), name='login'),
]

from django.urls import path
from . import views
import django.contrib.auth.views as view

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    # RESET PASWORD URL's
    path("password_change/",view.PasswordChangeView.as_view(), name="password_change"),
    path("password_reset/", view.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
] 

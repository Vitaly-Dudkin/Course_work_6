from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user_app.apps import UserAppConfig

app_name = UserAppConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

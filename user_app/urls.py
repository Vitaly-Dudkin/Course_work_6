from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user_app.apps import UserAppConfig
from user_app.views import RegisterView, verification, ProfileView, InfoView, UserListView, switch_status_user

app_name = UserAppConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/<str:verification_code>/', verification, name='verification'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('info_page/', InfoView.as_view(), name='info_page'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('switch_status_user/<int:pk>/', switch_status_user, name='switch_status_user'),

]

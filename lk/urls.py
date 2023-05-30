from django.urls import path, include
from .views import register, profile
from .views import UserLoginView, UserLogoutView, ProfileList, ProfileDetail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(template_name='lk/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='lk/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile_list/', ProfileList.as_view(), name='profile_list'),
    path('lk/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
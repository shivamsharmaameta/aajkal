from django.urls import path
from login_signup import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name = 'signup' ),
    path('accounts/login/', views.login_page, name = 'login' ),
    path('accounts/logout/', views.logout_page, name = 'logout' ),
    path('dashboard/', views.dashboard, name = 'dashboard' ),
]

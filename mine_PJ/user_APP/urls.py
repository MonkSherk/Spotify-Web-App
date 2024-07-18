from django.urls import path

from user_APP import views

urlpatterns = [
    path('register/', views.register_view, name='register_page'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
]

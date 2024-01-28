from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_user),
    path('logout', views.logout_user),
    path('register', views.register_user)
]

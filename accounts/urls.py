from django.urls import include, path

from accounts import views

urlpatterns = [
path('login', views.login, name="login"),
path('register', views.register, name="register"),
path('logout', views.logout, name="logout"),
path('success', views.success, name="success"),
]
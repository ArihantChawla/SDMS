from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard_17103036', views.dashboard_17103036, name='dashboard_17103036'),
    path('dashboard_17103042', views.dashboard_17103042, name='dashboard_17103042'),
]

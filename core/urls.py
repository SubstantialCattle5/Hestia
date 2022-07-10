from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('main', views.main_pg, name='main_pg'),
    path("problems", views.problems, name="problems"),
    path("solution", views.solution, name="solution"),

]

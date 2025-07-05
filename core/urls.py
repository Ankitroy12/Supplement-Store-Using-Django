from django.urls import path
from core import views

urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('protein',views.protein),
    path('creatine',views.creatine),
    path('supplements',views.supplements),
    path('contact',views.contact,name='contact'),
    path('medicine',views.medicine),
    path('register',views.register_view,name="register"),
    path('',views.login_view,name="login"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('dashboard',views.dashboard_view,name="dashboard"),
]

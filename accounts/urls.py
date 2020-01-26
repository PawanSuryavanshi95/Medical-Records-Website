from django.urls import path
from . import views

urlpatterns = [
    path('register1/',views.register1,name='register1'),
    path('login/',views.login,name='login'),
    path('register2/',views.register2,name='register2'),
    path('logout/',views.logout,name='logout'),
]
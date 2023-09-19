from . import views
from django.urls import path



urlpatterns = [

    path('new',views.new,name='new'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
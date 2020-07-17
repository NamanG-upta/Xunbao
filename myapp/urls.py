from django.conf.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # xunbao/
    path('', views.index, name='index'),

    # xunbao/login/
    path('login/', views.my_login, name='login'),

    # xunbao/leaderboard/
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # logout
    path('logout/', views.my_logout, name='logout'),

    # /xunbao/developers/
    path('developers/', views.developers, name='developers'),
    
    #api's
    path('getq/', views.User_list),
    path('checkans/', views.checkans),
    path('leaderboard_api/', views.lead_api),
    path('status/', views.status),
    path('logs/', views.logs_data),
]

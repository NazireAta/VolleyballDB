from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:number>', views.printNumber, name='printNumber'),
    path('<str:string', views.printString, name='printString'),

    path('login/', views.loginIndex, name='loginIndex'),
    path('login/#', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('dbManager/', views.dbManagerIndex, name='dbManagerIndex'),
    path('dbManager/#', views.dbManager, name='dbManager'),
    path('coach/', views.coachIndex, name='coachIndex'),
    path('coach/#', views.coach, name='coach'),
    path('jury/', views.juryIndex, name='juryIndex'),
    path('jury/#', views.jury, name='jury'),
    path('player/', views.playerIndex, name='playerIndex'),
    path('player/#', views.player, name='player'),
]

# basically, create urls and connect them to the views funcions
# then, connect the urls of the app to the urls of project
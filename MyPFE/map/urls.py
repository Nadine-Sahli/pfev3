from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login/', views.logine, name="login"),
    path('maps/<int:id>/', views.add_node, name='add_node'),
    path('compost/<str:pseudo>/', views.add_nodes, name='add_nodes'),
    path('interface/<int:id>/', views.interface, name='interface'),
    # path('client/', views.logineclient, name='logineclient'),
    path('composteur/', views.loginecomposteur, name='loginecomposteur'),
    path('open/', views.ouvrir_projet, name='open'),
    # path('co/<str:pseudo>/', views.sol, name='sol'),
    path('pri/', views.pri, name='pri'),
    path('co/', views.logout, name='logout'),
]

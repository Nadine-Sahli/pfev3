from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as mdp


urlpatterns = [
    path('login/', views.logine, name="login"),
    path('maps/<int:id>/', views.add_node, name='add_node'),
    path('compost/<str:pseudo>/', views.add_nodes, name='add_nodes'),
    path('interface/<int:id>/', views.interface, name='interface'),
    path('up/', views.my_view, name='my-view'),
    # path('client/', views.logineclient, name='logineclient'),
    path('composteur/', views.loginecomposteur, name='loginecomposteur'),
    path('open/', views.ouvrir_projet, name='open'),
    # path('co/<str:pseudo>/', views.sol, name='sol'),
    # path('nodes/<int:node_id>/', node_details, name='node_detail'),
    # path('co/', views.logout, name='logout'),
    path('chart/', chart_view, name='chart'),
    
    path('reset_password/', mdp.PasswordResetView.as_view(template_name='password_reset.html'), name="password-reset"),
    path('reset_password_done/', mdp.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', mdp.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', mdp.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

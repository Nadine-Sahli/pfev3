from django.urls import path, include
from . import views

urlpatterns = [
    path('_<str:pk>',views.compte,name='compte'),
    path('',views.compte,name='compte'),
    path('ajouprojet/',views.create_projet,name='create_projet'),
    path('ajo/',views.lister_projets,name='lister_projets'),
    path('open/',views.ouvrir_projet,name='client'),
    path('project_interface/',views.project_interface, name='project_interface'),
    path('step/',views.step, name='step'),
    path('o/',views.o, name='o'),
    # path('j/', views.chart, name='chart'),
    # path('project_list/',views.project_list, name='project_list'),
    path('projets/', views.lister_projets, name='lister_projets'),
    path('projets/delete/<int:projet_id>/', views.delete_projet, name='delete_projet'),
    path('projets/edit/<int:projet_id>/', views.edit_projet, name='edit_projet'),
    path('projets/update/<int:projet_id>/', views.update_projet, name='update_projet'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('interface/<int:id>/', views.post_list, name='interface'),
    #path('publish', views.publish_message, name='publish'),
    # path('interface/<int:id>/', views.post_list, name='interface'),
    path('UPdate/', views.start_mqtt, name='update'),
    # path('compost_report/', views.compost_report, name='compost_report'),
    # path('ht/', views.plot_temperature_humidity, name='ht'),
]

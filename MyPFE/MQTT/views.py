import matplotlib
matplotlib.use('Agg')
from django.conf import settings

import json
import random
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Post
from map.models import nodes
from .mqtt import start_mqtt_client

import matplotlib.pyplot as plt
import os
def start_mqtt(request):

    start_mqtt_client()

    return render(request, 'interface.html', {})

def post_list(request, id):

    node = nodes.objects.get(id=id)
    post = Post.objects.filter(po_id=node.id).order_by('-id').first()
    return render(request, 'interface.html', {'post': post})


# def plot_temperature_humidity(request):
#     # Récupérer les données de température et d'humidité depuis la base de données
#     temperature_data = []
#     humidity_data = []
#     time_data = []
#     posts = Post.objects.all()
#     for post in posts:
#         temperature_data.append(post.temperature)
#         humidity_data.append(post.humidity)
#         time_data.append(post.published_date)

#     # Créer un graphique d'humidité en fonction du temps
#     plt.figure(figsize=(10,5))
#     plt.plot(time_data, humidity_data, 'b.-')
#     plt.xlabel('Time')
#     plt.ylabel('Humidity')
#     plt.title('Humidity vs. Time')
#     plt.grid(True)
#     humidity_plot_path = os.path.join(settings.STATIC_ROOT, 'humidity_time_plot.png')
#     plt.savefig(humidity_plot_path)
    
#     # Créer un graphique de température en fonction du temps
#     plt.figure(figsize=(10,5))
#     plt.plot(time_data, temperature_data, 'r.-')
#     plt.xlabel('Time')
#     plt.ylabel('Temperature')
#     plt.title('Temperature vs. Time')
#     plt.grid(True)
#     temperature_plot_path = os.path.join(settings.STATIC_ROOT, 'temperature_time_plot.png')
#     plt.savefig(temperature_plot_path)
    
#     context = {
#         'humidity_plot_filename': os.path.relpath(humidity_plot_path, settings.STATIC_ROOT),
#         'temperature_plot_filename': os.path.relpath(temperature_plot_path, settings.STATIC_ROOT),
#     }
#     return render(request, 'plot.html', context)


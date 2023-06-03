from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import *
from django.contrib.gis.geos import Point
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from registre.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import nodes

def logine(request):
    return render(request,"interfacee.html")




def loginecomposteur(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo, password=mot_de_passe)       
            if data is not None:
                login(request, data)
            return redirect('add_nodes',pseudo)
        return render(request, 'login.html', {'form': formulaire})
        
    return render(request, 'login.html', {'form': LoginForm()})
@login_required
def sol(request, pseudo):
        
    return render(request,"mapp.html")
@login_required
def ouvrir_projet(request):
    if request.method == 'POST':
       
        data = request.POST

        # Retrieve the project object based on the project name and client name
        try:
            projet = Projet.objects.get(Nom_projet=data['nom_projet'], Nom=data['nom_client'])
        except Projet.DoesNotExist:
             return HttpResponse('projet introuvable.')
        
        if projet.pseudo != data['password']:
            return render(request, 'mauvais_mot_de_passe.html')
   
        return redirect('interface',  id=projet.id)
    else:
        
        return render(request, 'ouvrir_projet.html')




@login_required
def add_node(request,id):
    
    project_instance =Projet.objects.get(id=id)
    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        reference = request.POST['reference']
        node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude,référence =reference , proj=project_instance)
        node.save()



        return redirect('add_node',id)

    all_nodes = nodes.objects.all()

    return render(request, 'map.html', {'all_nodes': all_nodes})





# def interface(request, id):
#     project_instance = Projet.objects.get(id=id)
#     nodes_list = nodes.objects.filter(proj=project_instance).first
#     post = Post.objects.order_by('-id').first()
#     print(post)
#     return render(request, 'tm.html', {'nodes_list': nodes_list, 'projet': project_instance, 'post': post})
@login_required
def interface(request, id):
    project_instance = Projet.objects.get(id=id)
    nodes_list = nodes.objects.filter(proj=project_instance).first
    post = Post.objects.order_by('-id').first()
    print(post)
    
    # Récupérer toutes les instances de Post
    posts = Post.objects.all()

    # Extraire les valeurs de température
    temperatures = [post.temperature for post in posts]
    humidities = [post.humidity for post in posts]

    # Préparer les données pour le rendu de la vue
    context = {
        'nodes_list': nodes_list,
        'projet': project_instance,
        'post': post,
        'temperatures': temperatures,
        'humidities': humidities,
    }

    return render(request, 'tm.html', context)




# @login_required
# def add_nodes(request, pseudo):
#     if request.method == 'POST':
#         mylatitude = request.POST.get('Latitude') 
#         mylongitude = request.POST.get('Longitude') 
#         point = Point(x=float(mylongitude), y=float(mylatitude))
#         node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude)
#         node.save()
#         return redirect('add_node')

#     comp = composteur.objects.get(pseudo=pseudo)  # Retrieve the composteur object
#     projet = Projet.objects.get(composteur=comp)  # Retrieve the project associated with the composteur

#     # Filter the nodes based on the project
#     project_nodes = nodes.objects.filter(proj = projet)

#     return render(request, 'final.html', {'all_nodes': project_nodes})
@login_required
def add_nodes(request, pseudo):
    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude)
        node.save()
        return redirect('add_node')

    comp = composteur.objects.get(pseudo=pseudo)  # Retrieve the composteur object
    projets = Projet.objects.filter(composteur=comp)  # Retrieve all projects associated with the composteur

    # Collect all the nodes associated with the projects
    project_nodes = nodes.objects.filter(proj__in=projets)

    return render(request, 'final.html', {'all_nodes': project_nodes})


@login_required
def my_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'interface.html', context)
@login_required
def chart_view(request):
    # Récupérer toutes les instances de Post
    posts = Post.objects.all()

    # Extraire les valeurs de température
    temperatures = [post.temperature for post in posts]
    humidities = [post.humidity for post in posts]

    # Préparer les données pour le rendu de la vue
    context = {
        'temperatures': temperatures,
        'humidities': humidities,
    }

    return render(request, 'tm.html', context)





































from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import *
from django.contrib.gis.geos import Point
from MQTT.models import*
from django.http import HttpResponse

def logine(request):
    return render(request,"connect.html")
def logout(request):
    return render(request,"tes.html")
def loginecomposteur(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo, password=mot_de_passe)
            # project_instance =Projet.objects.all()
            # for pr in project_instance:
            #     idp=pr.id
            # comp= composteur.objects.get(pseudo=pseudo)
           
            if data is not None:
                login(request, data)
            return redirect('add_nodes',pseudo)
            #    id=id
        return render(request, 'login.html', {'form': formulaire})
        
    return render(request, 'login.html', {'form': LoginForm()})
# def sol(request, pseudo):
        
#     return render(request,"mapp.html")

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







def add_node(request,id):
    
    project_instance =Projet.objects.get(id=id)
    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        
        node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude,proj=project_instance)
        node.save()



        return redirect('add_node',id)

    all_nodes = nodes.objects.all()

    return render(request, 'map.html', {'all_nodes': all_nodes})





def interface(request, id):
    project_instance = Projet.objects.get(id=id)
    nodes_list = nodes.objects.filter(proj=project_instance).first
    post = Post.objects.order_by('-id').first()
    return render(request, 'interface.html', {'nodes_list': nodes_list, 'projet': project_instance, 'post': post})



def add_nodes(request,pseudo):
    

    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        
        node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude)
        node.save()



        return redirect('add_node')

    all_nodes = nodes.objects.all()

    return render(request, 'tes.html', {'all_nodes': all_nodes})




def pri(request):
    return render(request,'pr.html')
































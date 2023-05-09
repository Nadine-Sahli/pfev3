from django.shortcuts import render, redirect
from . import views
from . forms import *
from .models import *
from map.models import nodes
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def compte(request, pk):
    if pk == 'composteur':
        if request.method == 'POST':
            formulaire = Form_composteur(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'composteur'
                # return redirect('add_node', pseudo=pseudo)
                return redirect('loginecomposteur')




            return render(request, 'registre.html', {'form': formulaire})
        return render(request, 'registre.html', {'form': Form_composteur()})
    else:
        if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'client'
                return redirect('home')

            return render(request, 'registre.html', {'form': formulaire})
        return render(request, 'registre.html', {'form': Form_client()})
    
def create_projet(request):
    if request.method == 'POST':
 
        Nom_projet = request.POST['Nom_projet']
        Nom = request.POST['Nom']
        prenom = request.POST['prenom']
        NB_GSM = request.POST['NB_GSM']
        pseudo = request.POST['pseudo']
        email = request.POST['e_mail']
        reference = request.POST['reference']
        password = request.POST['password']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        nouveau_projet = Projet(
            Nom_projet=Nom_projet,
            Nom=Nom,
            prenom=prenom,
            NB_GSM=NB_GSM,
            pseudo=pseudo,
            e_mail=email,
            reference=reference,
            password=password,
        )
      
        nouveau_projet.save()

        nouveau_projet.id = nouveau_projet.pk
        
        nouveau_projet.save()
        
        return redirect('add_node',id=nouveau_projet.id)
    else:
        return render(request, 'step1.html') 



def lister_projets(request):

    projets = Projet.objects.all()

    return render(request, 'step2.html', {'projets': projets})

# def project_list(request):
#     projects = Projet.objects.all()
#     project_name = request.GET.get('project_name')
#     if project_name:
#         projects = projects.filter(Nom_projet__icontains=project_name)
#     return render(request, 'project_list.html', {'projects': projects})





def ouvrir_projet(request):
    us=request.user.id
    print(us)
    # project_instance =projet.objects.get(id=request.user.id)
    if request.method == 'POST':
        prenom = request.POST['nom_projet']
        data = request.POST
        print(data)
        print(prenom)
        try:
            projet = Projet.objects.get(Nom_projet=data['nom_projet'], Nom=data['nom_client'])
        except Projet.DoesNotExist:
             return HttpResponse('projet introuvable.')
        if projet.pseudo != data['password']:
            return render(request, 'mauvais_mot_de_passe.html')
   
        return redirect('interface',  id=projet.id)
    else:
        
        return render(request, 'ouvrir_projet.html')



   
def project_interface(request):

    node = nodes.objects.order_by('-id').first() 

    if request.method == 'POST':
  
        project_name = request.POST.get('Nom_projet')
        client_name = request.POST.get('Nom')
        password = request.POST.get('password')
        
     
        try:
            project = Projet.objects.get(Nom_projet=project_name, Nom=client_name, password=password)
        except Projet.DoesNotExist:
            return HttpResponse('Invalid project name, client name, or password.')
        
        context = {
            'project_name': project.Nom_projet,
            'client_name': project.Nom,
            'num_gsm': project.GSM,
            'pseudo': project.pseudo,
            'email': project.e_mail,
            'reference': project.reference,
            'node':node
        }

        return render(request, 'interface.html', context)
    else:
        # Show the form to open a specific project interface
        return render(request, 'map.html')


def step(request):
    return render(request, "step2.html")

def o(request):
    return render(request, "o.html")
    

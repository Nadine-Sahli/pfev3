from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from map.models import nodes

@login_required
def compte(request, pk):
    if pk == 'composteur':
        if request.method == 'POST':
            formulaire = Form_composteur(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'composteur'
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

@login_required
def create_projet(request):
    compos = request.user  # Récupérer le composteur associé à l'utilisateur connecté
    print(compos)
    if request.method == 'POST':
        Nom_projet = request.POST['Nom_projet']
        Nom = request.POST['Nom']
        prenom = request.POST['prenom']
        NB_GSM = request.POST['NB_GSM']
        pseudo = request.POST['pseudo']
        email = request.POST['e_mail']
        reference = request.POST['reference']
        password = request.POST['password']
        # start_date = request.POST['start_date']
        # end_date = request.POST['end_date']

       
        comp = composteur.objects.get(pseudo=compos)
        nouveau_projet = Projet(
            Nom_projet=Nom_projet,
            Nom=Nom,
            prenom=prenom,
            NB_GSM=NB_GSM,
            pseudo=pseudo,
            e_mail=email,
            reference=reference,
            password=password,
            composteur=comp,  # Associer le composteur au projet
        )
        nouveau_projet.save()
        nouveau_projet.id = nouveau_projet.pk
        nouveau_projet.save()
        return redirect('add_node', id=nouveau_projet.id)
    else:
        return render(request, 'step1.html')


@login_required
def lister_projets(request):
    comp = request.user.username
    print(comp)
    projets = Projet.objects.filter(composteur__pseudo = comp)
    return render(request, 'lp.html', {'projets': projets})

@login_required
def delete_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    projet.delete()
    return redirect('lister_projets')

@login_required
def edit_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    return render(request, 'edit_projet.html', {'projet': projet})

@login_required
def update_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)

    if request.method == 'POST':
        nom_projet = request.POST['Nom_projet']
        nom = request.POST['Nom']
        prenom = request.POST['prenom']
        nb_gsm = request.POST['NB_GSM']
        pseudo = request.POST['pseudo']
        e_mail = request.POST['e_mail']
        reference = request.POST['reference']
        password = request.POST['password']

        # start_date = datetime.strptime(start_date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        # end_date = datetime.strptime(end_date_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        projet.Nom_projet = nom_projet
        projet.Nom = nom
        projet.prenom = prenom
        projet.NB_GSM = nb_gsm
        projet.pseudo = pseudo
        projet.e_mail = e_mail
        projet.reference = reference
        # projet.start_date = start_date
        # projet.end_date = end_date
        # projet.password = password

        projet.save()

        return redirect('lister_projets')

    else:
        return render(request, 'edit_projet.html', {'projet': projet})

@login_required
def ouvrir_projet(request):
    us = request.user.id
    print(us)
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
        return redirect('interface', id=projet.id)
    else:
        return render(request, 'ouvrir_projet.html')

@login_required  
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
            'num_gsm': project.NB_GSM,
            'pseudo': project.pseudo,
            'email': project.e_mail,
            'reference': project.reference,
            'node': node
        }
        return render(request, 'interface.html', context)
    else:
        return render(request, 'map.html')

@login_required
def step(request):
    return render(request, "step2.html")

@login_required
def o(request):
    return render(request, "o.html")

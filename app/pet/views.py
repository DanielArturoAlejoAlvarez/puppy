# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from django.http import HttpResponse

from app.pet.forms import PetForm

from app.pet.models import Pet

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from django.core import serializers

from django.contrib.auth.models import User 

# Create your views here.
def listUser(request):
	list=serializers.serialize('json', User.objects.all(), fields=['first_name', 'last_name', 'email', 'username'])
	return HttpResponse(list, content_type='application/json')

def index(request):
	#return HttpResponse("<h1>Pets</h1>")
	return render(request, 'pet/index.html')

def pet_view(request):
	if request.method=='POST':
		form=PetForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('pet:pet_to_list')
	else:
		form=PetForm()

	return render(request, 'pet/pet_form.html', {'form':form})

def pet_list(request):
	pet=Pet.objects.all().order_by('id')
	context={'pets':pet}
	return render(request, 'pet/pet_list.html', context)

def pet_edit(request, id_pet):
	pet=Pet.objects.get(id=id_pet)
	if request.method=='GET':
		form=PetForm(instance=pet)
	else:
		form=PetForm(request.POST, instance=pet)
		if form.is_valid():
			form.save()
		return redirect('pet:pet_to_list')
	return render(request, 'pet/pet_form.html', {'form':form})

def pet_delete(request, id_pet):
	pet=Pet.objects.get(id=id_pet)
	if request.method=='POST':
		pet.delete()
		return redirect('pet:pet_to_list')
	return render(request, 'pet/pet_delete.html', {'pet':pet})



############################################################################################################################################################

class PetList(ListView):
	model=Pet
	template_name='pet/pet_list.html'
	paginate_by=1

class PetCreate(CreateView):
	model=Pet
	form_class=PetForm
	template_name='pet/pet_form.html'
	success_url=reverse_lazy('pet:pet_to_list')

class PetUpdate(UpdateView):
	model=Pet
	form_class=PetForm
	template_name='pet/pet_form.html'
	success_url=reverse_lazy('pet:pet_to_list')

class PetDelete(DeleteView):
	model=Pet
	template_name='pet/pet_delete.html'
	success_url=reverse_lazy('pet:pet_to_list')
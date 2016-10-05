# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.adoption.models import Person, YourRequest

from django.core.urlresolvers import reverse_lazy

from app.adoption.forms import PersonForm, YourRequestForm

# Create your views here.



def index_adoption(request):
	return HttpResponse("<h2>Homepage of my app with Django Python Framework.</h2>")

class YourRequestList(ListView):
	model=YourRequest
	template_name='adoption/your_request_list.html'

class YourRequestCreate(CreateView):
	model=YourRequest
	form_class=YourRequestForm
	second_form_class=PersonForm
	template_name='adoption/your_request_form.html'	
	success_url=reverse_lazy('adoption:your_request_to_list')

	def get_context_data(self, **kwargs):
		context=super(YourRequestCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object=self.get_object
		form=self.form_class(request.POST)
		form2=self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			yr=form.save(commit=False)
			yr.person=form2.save()
			yr.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_respose(self.get_context_data(form=form, form2=form2))



class YourRequestUpdate(UpdateView):
	model=YourRequest
	second_model=Person
	form_class=YourRequestForm
	second_form_class=PersonForm
	template_name='adoption/your_request_form.html'
	success_url=reverse_lazy('adoption:your_request_to_list')

	def get_context_data(self, **kwargs):
		context=super(YourRequestUpdate, self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk', 0)
		yr=self.model.objects.get(id=pk)
		p=self.second_model.objects.get(id=yr.person_id)
		if 'form' not in context:
			context['form']=self.form_class()
		if 'form2'not in context:
			context['form2']=self.second_form_class(instance=p)
		context['id']=pk
		return context

	def post(self, request, *args, **kwargs):
		self.object=self.get_object
		id_yr=kwargs['pk']
		yr=self.model.objects.get(id=id_yr)
		p=self.second_model.objects.get(id=yr.person_id)
		form=self.form_class(request.POST, instance=yr)
		form2=self.second_form_class(request.POST, instance=p)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class YourRequestDelete(DeleteView):
	model=YourRequest
	template_name='adoption/your_request_delete.html'
	success_url=reverse_lazy('adoption:your_request_to_list')
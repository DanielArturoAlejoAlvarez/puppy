# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy

from app.all_user.forms import RegisterAllUserForm

#REST
from rest_framework.views import APIView
from app.all_user.serializers import UserSerializer
import json
from django.http import HttpResponse
# Create your views here.

class RegisterAllUser(CreateView):
	model=User
	template_name='all_user/all_user_form.html'
	#form_class=UserCreationForm
	form_class=RegisterAllUserForm
	success_url=reverse_lazy('pet:pet_to_list')

#REST
class UserAPI(APIView):
	serializer=UserSerializer

	def get(self, request, format=None):
		list=User.objects.all()
		response=self.serializer(list, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
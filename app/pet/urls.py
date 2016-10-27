from django.conf.urls import url, include

from app.pet.views import listUser, index, pet_view, pet_list, pet_edit, pet_delete,\
	PetList, PetCreate, PetUpdate, PetDelete

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^new$', pet_view, name='pet_create'),
    url(r'^new$', login_required(PetCreate.as_view()), name='pet_create'),
    #url(r'^to_list$', pet_list, name='pet_to_list'),
    #url(r'^to_list$', login_required(PetList.as_view()), name='pet_to_list'),
    url(r'^to_list', login_required(PetList.as_view()), name='pet_to_list'),
    #url(r'^to_edit/(?P<id_pet>\d+)/$', pet_edit, name='pet_to_edit'),
    url(r'^to_edit/(?P<pk>\d+)/$', login_required(PetUpdate.as_view()), name='pet_to_edit'), 
    #url(r'^to_delete/(?P<id_pet>\d+)/$', pet_delete, name='pet_to_delete'),
    url(r'^to_delete/(?P<pk>\d+)/$', login_required(PetDelete.as_view()), name='pet_to_delete'),


    url(r'^list$', listUser, name="list"),
]

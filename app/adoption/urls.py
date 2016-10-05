from django.conf.urls import url 

from app.adoption.views import index_adoption, YourRequestList, YourRequestCreate, YourRequestUpdate, YourRequestDelete

urlpatterns = [
     url(r'^index$', index_adoption),
     url(r'^your_request/to_list$', YourRequestList.as_view(), name='your_request_to_list'),
     url(r'^your_request/new$', YourRequestCreate.as_view(), name='your_request_create'),
     url(r'^your_request/to_edit/(?P<pk>\d+)/$', YourRequestUpdate.as_view(), name='your_request_to_edit'),
     url(r'^your_request/to_delete/(?P<pk>\d+)/$', YourRequestDelete.as_view(), name='your_request_to_delete'),
]



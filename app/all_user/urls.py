from django.conf.urls import url

from app.all_user.views import RegisterAllUser, UserAPI


urlpatterns = [

	url(r'^to_register$', RegisterAllUser.as_view(), name='to_register'),

	url(r'^api', UserAPI.as_view(), name='api'),

]
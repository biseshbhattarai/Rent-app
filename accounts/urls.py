from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name_ = 'accounts'


urlpatterns = [
	url(r'^login/',auth_views.login ,{'template_name':'login.html'},name='login'),
	url(r'^logout/',auth_views.logout ,{'template_name':'logout.html'},name='logout'),
	url(r'^signin/$',views.register ,name='register'),


	

]


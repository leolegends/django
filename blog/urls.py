from django.conf.urls import url
from blog import views
from blog.controllers import homeController as home

'''
Trabalhando com homeController.
'''

urlpatterns = [
	url(r'^$', home.inicio)
	]
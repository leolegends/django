from django.conf.urls import url

from blog import views
from blog import homeController

urlpatterns = [
	url(r'^$', homeController.home),
	url('numerais/', views.numerais),
]
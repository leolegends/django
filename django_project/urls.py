from django.conf.urls import url, include
from django.contrib import admin
from blog.controllers import homeController as home

urlpatterns = [
	# Rota direcionada para HomeController
	url(r'^$', home.inicio),
    url(r'^admin/', admin.site.urls),
    # Grupo de rotas direcionada para blog URL
    url(r'^blog/', include('blog.urls'))
]

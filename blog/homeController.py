# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category

'''
esse ultimo import eu chamei a model que eu quero trabalhar
'''

def home(request):


# Aqui eu faço uma query all() la na model category

	category = Category.objects.all()

	# languages = [
	# 'Python', 'PHP', 'JavaScript', 'NodeJS'
	# ]

	# for language in languages:
	# 	Category.objects.create(name=lang)

	context = {
		'categories': category
	}

# aqui eu crio um registro na model category 
# Category.objects.create(name="Python")

	return render(request, 'blog/home.html', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category, Post

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


	# para pegar o post com a primary key = 1 usamos:
	# post = Post.objects.get(pk=1)

	# Para pegar categoria 

	category_python = Category.objects.get(name='PHP')

	post = Post()
	post.name = "Leonardo Ribeiro"
	post.content = "Minha tia se chama Deiliete"
	post.status = "Published"
	post.category = category_python
	post.save()


	# Viu que louco? nao precisei passar id, atribui o proprio objeto.


	context = {
		'categories': category,
		'post': post
	}

# aqui eu crio um registro na model category 
# Category.objects.create(name="Python")

	return render(request, 'blog/home.html', context)

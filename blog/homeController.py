# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def home(request):

	name = [
	"Leonardo Ribeiro",
	"Gabriel Sousa",
	"Gabriela Lima"
	]

	languages = [
	'Python', 'PHP', 'JavaScript', 'NodeJS'
	]

	context = {
		'names': name,
		'languages': languages
	}

	return render(request, 'blog/home.html', context)

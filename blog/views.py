# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def numerais(request):
	lista = range(1,1000)
	context = {
		'numerais': lista 
	}

	return HttpResponse(lista)

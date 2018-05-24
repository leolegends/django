# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return HttpResponse("Olha lá, olha só")

def idade(request):
	return HttpResponse("18 anos")

def nome(request):
	return HttpResponse("Gabriela")

def email(request):
	return HttpResponse("gabrielalima558@gmail")

def nomeDaMae(request):
	return HttpResponse("Elaine")

def nomeDoPai(request):
	return HttpResponse("Vilmar")
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=255)

	# Toda vez que chamar esse model, ele vai retornar o nome do objeto.
	# a funcao abaixo serve pra isso
	def __unicode__(self):
		return self.name

class Post(models.Model):

	# AQUI EM CIMA EU CONSIGO CRIAR UMA CHAVE ESTRANGEIRA FACILMENTE
	# EU CRIO UMA COLUNA CHAMADA CATEGORY QUE E UMA FOREIGNKEY LIGADA NA MODEL CATEGORY.

	category = models.ForeignKey(Category)
	name = models.CharField(max_length=255)
	content = models.TextField()
	# Esse STATUS_CHOICE E UMA TUPLA DE OPCAO, ONDE ESTOU DIZENDO QUE ESSA COLUNA NO BANCO 
	# NÃO PODE SER MODIFICADA, APENAS UM SELECT COM ESSAS OPCOES 
	STATUS_CHOICE = (
		('Draft','Draft'),
		('Publish','Publish')
	)

	# AQUI EMBAIXO EU CRIO UMA COLUNA CHAMADA STATUS NO BANCO, QUE RECEBE A TUPLA ACIMA
	# COM VALOR DEFAULT DE DRAFT

	status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Draft')
	created_at = models.DateTimeField(auto_now_add=True)

	# Toda vez que chamar esse model, ele vai retornar o nome do objeto.
	# a funcao abaixo serve pra isso
	def __unicode__(self):
		return self.content
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Category, Post
from django.contrib import admin

# Esse admin.py serve para registrar as models que irao aparecer no painel administrativo.

class PostAdmin(admin.ModelAdmin):
	list_display = ('name','status','category')
	search_fields = ['id','name', 'content']
	list_filter = ['status','category', 'created_at']

# Com essa classe, conseguimos exibir as colunas no painel administrativo,
# ficando mais visual e pratico.
# e depois passamos ela como segundo atributo do admin.site.register do post.
# Search Fields é o campo de busca, e o que ele ira procurar.
# list_filter aparece um painel ao lado que filtra facilmente os dados que estao
# sendo passados no array.


admin.site.register(Category)
admin.site.register(Post, PostAdmin)




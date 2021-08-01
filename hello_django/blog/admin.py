from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): #os campos que aparece na tela
    list_display = ("title","slug","author","created","updated")
    prepopulated_fields = {"slug":("title",)} #conforme for escrevendo os titulos o slug vai att automaticamente



from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse 

class Post(models.Model): #criando uma tabela no banco de dados pra armazenar os posts
    title = models.CharField(max_length=255)  #diz que o campo tem que receber strings ate 255 de tamanho
    slug = models.SlugField(max_length=255, unique=True) #È o texto que vamos usar nas urls
    author = models.ForeignKey(User, on_delete=models.CASCADE) #vai guardar o id do author do post
    body = models.TextField() # o corpo do post, author pode escrever o quanto quiser
    created = models.DateTimeField(auto_now_add=True) # vai add automaticamente a data e a hora que o artigo foi criado
    updated = models.DateTimeField(auto_now=True) #vai mostrar a data e hora da ultima att automatico

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse("blog:detail", kwargs={"slug": self.slug}) 

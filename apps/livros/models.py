from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    nome = models.CharField(max_length=150)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    nacionalidade = models.CharField(max_length=50)
    sexo = models.CharField(choices=SEXO, max_length=150)

    class Meta():
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)

    class Meta():
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    qtd_paginas = models.IntegerField(verbose_name="Quantidade de páginas")
    ano_pub = models.IntegerField(verbose_name="Ano de publicação")
    resenha = models.TextField()
    autor = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    capa = models.ImageField(upload_to='capas/')
    onde_comprar = models.URLField(verbose_name="Onde comprar")
    livro_pdf = models.FileField(upload_to='livros/', verbose_name="Livro em PDF")
    publicado = models.BooleanField(default=False, verbose_name="Publicar livro")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta():
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

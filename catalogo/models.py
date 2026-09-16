from django.db import models


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    genero = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    nota = models.IntegerField()
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
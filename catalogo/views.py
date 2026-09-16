from django.shortcuts import render, redirect
from .models import Jogo


def lista_jogos(request):
    jogos = Jogo.objects.all()

    return render(request, 'catalogo/lista_jogos.html', {'jogos': jogos})


def adicionar_jogo(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        genero = request.POST['genero']
        status = request.POST['status']
        nota = request.POST['nota']

        Jogo.objects.create(
            nome=nome,
            descricao=descricao,
            genero=genero,
            status=status,
            nota=nota
        )

        return redirect('lista_jogos')

    return render(request, 'catalogo/adicionar_jogo.html')

def excluir_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()

    return redirect('lista_jogos')
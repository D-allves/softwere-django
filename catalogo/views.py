```python
from django.shortcuts import render, redirect
from .models import Jogo
from django.db.models import Avg


def lista_jogos(request):
    busca = request.GET.get('busca', '')
    status = request.GET.get('status', '')
    ordem = request.GET.get('ordem', '')

    jogos = Jogo.objects.all()

    if busca:
        jogos = jogos.filter(nome__icontains=busca)

    if status:
        jogos = jogos.filter(status__icontains=status)

    if ordem == 'maior':
        jogos = jogos.order_by('-nota')
    elif ordem == 'menor':
        jogos = jogos.order_by('nota')

    total_jogos = Jogo.objects.count()
    media = Jogo.objects.aggregate(Avg('nota'))['nota__avg']

    if media is not None:
        media = round(media, 1)

    return render(request, 'catalogo/lista_jogos.html', {
        'jogos': jogos,
        'busca': busca,
        'status': status,
        'ordem': ordem,
        'total_jogos': total_jogos,
        'media': media
    })


def adicionar_jogo(request):
    erro = None

    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        genero = request.POST['genero']
        status = request.POST['status']
        nota = int(request.POST['nota'])

        if nota < 0 or nota > 10:
            erro = 'A nota deve estar entre 0 e 10.'

        else:
            Jogo.objects.create(
                nome=nome,
                descricao=descricao,
                genero=genero,
                status=status,
                nota=nota
            )

            return redirect('lista_jogos')

    return render(request, 'catalogo/adicionar_jogo.html', {
        'erro': erro
    })


def excluir_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()

    return redirect('lista_jogos')


def editar_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    erro = None

    if request.method == 'POST':
        jogo.nome = request.POST['nome']
        jogo.descricao = request.POST['descricao']
        jogo.genero = request.POST['genero']
        jogo.status = request.POST['status']
        jogo.nota = int(request.POST['nota'])

        if jogo.nota < 0 or jogo.nota > 10:
            erro = 'A nota deve estar entre 0 e 10.'

        else:
            jogo.save()

            return redirect('lista_jogos')

    return render(request, 'catalogo/editar_jogo.html', {
        'jogo': jogo,
        'erro': erro
    })
```

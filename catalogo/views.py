
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Jogo


@login_required
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


@login_required
def adicionar_jogo(request):
    if request.method == 'POST':
        Jogo.objects.create(
            nome=request.POST['nome'],
            descricao=request.POST['descricao'],
            genero=request.POST['genero'],
            status=request.POST['status'],
            nota=request.POST['nota']
        )
        return redirect('lista_jogos')

    return render(request, 'catalogo/adicionar_jogo.html')


@login_required
def excluir_jogo(request, id):
    jogo = get_object_or_404(Jogo, id=id)

    if request.method == 'POST':
        jogo.delete()

    return redirect('lista_jogos')


@login_required
def editar_jogo(request, id):
    jogo = get_object_or_404(Jogo, id=id)

    if request.method == 'POST':
        jogo.nome = request.POST['nome']
        jogo.descricao = request.POST['descricao']
        jogo.genero = request.POST['genero']
        jogo.status = request.POST['status']
        jogo.nota = request.POST['nota']
        jogo.save()

        return redirect('lista_jogos')

    return render(request, 'catalogo/editar_jogo.html', {
        'jogo': jogo
    })
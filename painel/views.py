from django.shortcuts import render, get_object_or_404, redirect
from painel.forms import CadastroVisitanteForm
from painel.models import CadastroVisitantes
from painel.models import CadastroMorador
from painel.models import CadastroCarros
from painel.models import CadastroFornecedores
from painel.models import AcessoVisitante
from painel.models import AcessoMorador
from painel.models import AcessoFornecedor
from painel.models import AcessoCarro
from painel.forms import CadastroMoradorForm
from painel.forms import CadastroFornecedoresForm
from painel.forms import CadastroCarrosForm
from painel.forms import AcessoCarroForm
from painel.forms import AcessoFornecedorForm
from painel.forms import AcessoMoradorForm
from painel.forms import AcessoVisitanteForm
from painel.models import Diario
from painel.models import Mensagem
from painel.forms import DiarioForm
from painel.forms import MensagemForm




def painel(request):
    return render(request, "painel.html")

def login(request):
    return render(request, "login.html")

def verVisitante(request):
    return render(request, "verVisitante.html")

def verMorador(request):
    return render(request, "verMorador.html")

def verFornecedor(request):
    return render(request, "verFornecedor.html")

def verCarros(request):
    return render(request, "verCarros.html")

def suporte(request):
    return render(request, "suporte.html")

def adicionaMensagem(request):
    if request.method == "POST": # Formulário enviado
        form = MensagemForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = MensagemForm()
    return render(request, "adicionaMensagem.html", {'form': form})

def adicionaDiario(request):
    if request.method == "POST": # Formulário enviado
        form = DiarioForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = DiarioForm()
    return render(request, "adicionarDiario.html", {'form': form})

def adicionaCadastroVisitantes(request):
    if request.method == "POST": # Formulário enviado
        form = CadastroVisitanteForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = CadastroVisitanteForm()
    return render(request, "adicionaCadastroVisitante.html", {'form': form})

def adicionaCadastroMorador(request):
    if request.method == "POST": # Formulário enviado
        form = CadastroMoradorForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = CadastroMoradorForm()
    return render(request, "adicionaCadastroMorador.html", {'form': form})

def adicionaCadastroFornecedor(request):
    if request.method == "POST": # Formulário enviado
        form = CadastroFornecedoresForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = CadastroFornecedoresForm()
    return render(request, "adicionaCadastroFornecedor.html", {'form': form})

def adicionaCadastroCarros(request):
    if request.method == "POST": # Formulário enviado
        form = CadastroCarrosForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = CadastroCarrosForm()
    return render(request, "adicionaCadastroCarros.html", {'form': form})

def adicionaAcessoVisitante(request):
    if request.method == "POST": # Formulário enviado
        form = AcessoVisitanteForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = AcessoVisitanteForm()
    return render(request, "adicionaAcessoVisitante.html", {'form': form})

def adicionaAcessoMoradores(request):
    if request.method == "POST": # Formulário enviado
        form = AcessoMoradorForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = AcessoMoradorForm()
    return render(request, "adicionaAcessoMorador.html", {'form': form})

def adicionaAcessoFornecedor(request):
    if request.method == "POST": # Formulário enviado
        form = AcessoFornecedorForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = AcessoFornecedorForm()
    return render(request, "adicionaAcessoFornecedor.html", {'form': form})

def adicionaAcessoCarro(request):
    if request.method == "POST": # Formulário enviado
        form = AcessoCarroForm(request.POST)
        if form.is_valid(): # Formulário válido
            form.save() # Salva o formulário

            # Mensagem de formulário cadastrado
            return render(request, "salvo.html", {})
    else: # Página acessada via link (método GET)
        # Exibe o formulário em branco
        form = AcessoCarroForm()
    return render(request, "adicionaAcessoCarro.html", {'form': form})

def listaDiario(request):
    listaDiario_itens = Diario.objects.all()
    return render(request, "listaDiario.html", {'listaDiario_itens': listaDiario_itens})

def listaMensagem(request):
    listaMensagem_itens = Mensagem.objects.all()
    return render(request, "listaMensagem.html", {'listaMensagem_itens': listaMensagem_itens})

def listaCadastroVisitantes(request):
    listaCadastroVisitantes_itens = CadastroVisitantes.objects.all()
    return render(request, "listaCadastroVisitantes.html", {'listaCadastroVisitantes_itens': listaCadastroVisitantes_itens})

def listaCadastroFornecedores(request):
    listaCadastroFornecedores_itens = CadastroFornecedores.objects.all()
    return render(request, "listaCadastroFornecedores.html", {'listaCadastroFornecedores_itens': listaCadastroFornecedores_itens})

def listaAcessoVisitantes(request):
    listaAcessoVisitantes_itens = AcessoVisitante.objects.all()
    return render(request, "listaAcessoVisitantes.html", {'listaAcessoVisitantes_itens': listaAcessoVisitantes_itens})

def listaAcessoCarros(request):
    listaAcessoCarros_itens = AcessoCarro.objects.all()
    return render(request, "listaAcessoCarros.html", {'listaAcessoCarros_itens': listaAcessoCarros_itens})

def listaAcessoFornecedores(request):
    listaAcessoFornecedores_itens = AcessoFornecedor.objects.all()
    return render(request, "listaAcessoFornecedores.html", {'listaAcessoFornecedores_itens': listaAcessoFornecedores_itens})

def itemCadastroVisitantes(request, nr_item):
    itemCadastroVisitantes = get_object_or_404(CadastroVisitantes, pk=nr_item)
    return render(request, "itemCadastroVisitantes.html", {'itemCadastroVisitantes': itemCadastroVisitantes})

def listaCadastroCarros(request):
    listaCadastroCarros_itens = CadastroCarros.objects.all()
    return render(request, "listaCadastroCarros.html", {'listaCadastroCarros_itens': listaCadastroCarros_itens})

def listaCadastroMoradores(request):
    listaCadastroMoradores_itens = CadastroMorador.objects.all()
    return render(request, "listaCadastroMoradores.html", {'listaCadastroMoradores_itens': listaCadastroMoradores_itens})

def listaAcessoMoradores(request):
    listaAcessoMoradores_itens = AcessoMorador.objects.all()
    return render(request, "listaAcessoMoradores.html", {'listaAcessoMoradores_itens': listaAcessoMoradores_itens})

def atualizaDiario(request, nr_item):
    itemDiario = get_object_or_404(Diario, pk=nr_item)
    form = DiarioForm(request.POST or None, instance=itemDiario)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaDiario.html", {'itemDiario': itemDiario, 'form': form})


def atualizaMensagem(request, nr_item):
    itemMensagem = get_object_or_404(Mensagem, pk=nr_item)
    form = MensagemForm(request.POST or None, instance=itemMensagem)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaMensagem.html", {'itemMensagem': itemMensagem, 'form': form})

def atualizaCadastroVisitantes(request, nr_item):
    itemCadastroVisitantes = get_object_or_404(CadastroVisitantes, pk=nr_item)
    form = CadastroVisitanteForm(request.POST or None, instance=itemCadastroVisitantes)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaCadastroVisitantes.html", {'itemCadastroVisitantes': itemCadastroVisitantes, 'form': form})

def atualizaCadastroFornecedores(request, nr_item):
    itemCadastroFornecedores = get_object_or_404(CadastroFornecedores, pk=nr_item)
    form = CadastroFornecedoresForm(request.POST or None, instance=itemCadastroFornecedores)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaCadastroFornecedores.html", {'itemCadastroFornecedores': itemCadastroFornecedores, 'form': form})

def atualizaCadastroCarros(request, nr_item):
    itemCadastroCarros = get_object_or_404(CadastroCarros, pk=nr_item)
    form = CadastroCarrosForm(request.POST or None, instance=itemCadastroCarros)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaCadastroCarros.html", {'itemCadastroCarros': itemCadastroCarros, 'form': form})


def atualizaCadastroMoradores(request, nr_item):
    itemCadastroMoradores = get_object_or_404(CadastroMorador, pk=nr_item)
    form = CadastroMoradorForm(request.POST or None, instance=itemCadastroMoradores)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaCadastroMoradores.html", {'itemCadastroMorador': itemCadastroMoradores, 'form': form})

def atualizaAcessoMoradores(request, nr_item):
    itemAcessoMoradores = get_object_or_404(AcessoMorador, pk=nr_item)
    form = AcessoMoradorForm(request.POST or None, instance=itemAcessoMoradores)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaAcessoMoradores.html", {'itemAcessoMorador': itemAcessoMoradores, 'form': form})

def atualizaAcessoCarros(request, nr_item):
    itemAcessoCarros = get_object_or_404(AcessoCarro, pk=nr_item)
    form = AcessoCarroForm(request.POST or None, instance=itemAcessoCarros)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaAcessoCarros.html", {'itemAcessoCarros': itemAcessoCarros, 'form': form})

def atualizaAcessoVisitante(request, nr_item):
    itemAcessoVisitantes = get_object_or_404(AcessoVisitante, pk=nr_item)
    form = AcessoVisitanteForm(request.POST or None, instance=itemAcessoVisitantes)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaAcessoVisitantes.html", {'itemAcessoVisitantes': itemAcessoVisitantes, 'form': form})

def atualizaAcessoFornecedores(request, nr_item):
    itemAcessoFornecedores = get_object_or_404(AcessoFornecedor, pk=nr_item)
    form = AcessoFornecedorForm(request.POST or None, instance=itemAcessoFornecedores)
    if form.is_valid():
        form.save()
        return redirect('/painel/')
    return render(request, "atualizaAcessoFornecedores.html", {'itemAcessoFornecedores': itemAcessoFornecedores, 'form': form})

def excluiDiario(request, nr_item):
    print(nr_item)
    itemDiario = get_object_or_404(Diario, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemDiario.delete()
        return redirect('/painel/')
    return render(request, "excluiDiario.html", {'itemDiario': itemDiario})

def excluiMensagem(request, nr_item):
    print(nr_item)
    itemMensagem = get_object_or_404(Mensagem, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemMensagem.delete()
        return redirect('/painel/')
    return render(request, "excluiMensagem.html", {'itemMensagem': itemMensagem})

def excluiCadastroVisitantes(request, nr_item):
    print(nr_item)
    itemCadastroVisitantes = get_object_or_404(CadastroVisitantes, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemCadastroVisitantes.delete()
        return redirect('/painel/')
    return render(request, "excluiCadastroVisitantes.html", {'itemCadastroVisitantes': itemCadastroVisitantes})

def excluiCadastroFornecedores(request, nr_item):
    print(nr_item)
    itemCadastroFornecedores = get_object_or_404(CadastroFornecedores, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemCadastroFornecedores.delete()
        return redirect('/painel/')
    return render(request, "excluiCadastroFornecedores.html", {'itemCadastroFornecedores': itemCadastroFornecedores})

def excluiCadastroMorador(request, nr_item):
    print(nr_item)
    itemCadastroMorador = get_object_or_404(CadastroMorador, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemCadastroMorador.delete()
        return redirect('/painel/')
    return render(request, "excluiCadastroMorador.html", {'itemCadastroMorador': itemCadastroMorador})


def excluiCadastroCarros(request, nr_item):
    print(nr_item)
    itemCadastroCarros = get_object_or_404(CadastroCarros, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemCadastroCarros.delete()
        return redirect('/painel/')
    return render(request, "excluiCadastroCarros.html", {'itemCadastroCarros': itemCadastroCarros})

def excluiAcessoMorador(request, nr_item):
    print(nr_item)
    itemAcessoMorador = get_object_or_404(AcessoMorador, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemAcessoMorador.delete()
        return redirect('/painel/')
    return render(request, "excluiAcessoMorador.html", {'itemAcessoMorador': itemAcessoMorador})

def excluiAcessoVisitantes(request, nr_item):
    print(nr_item)
    itemAcessoVisitantes = get_object_or_404(AcessoVisitante, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemAcessoVisitantes.delete()
        return redirect('/painel/')
    return render(request, "excluiAcessoVisitantes.html", {'itemAcessoVisitantes': itemAcessoVisitantes})

def excluiAcessoFornecedores(request, nr_item):
    print(nr_item)
    itemAcessoFornecedores = get_object_or_404(AcessoFornecedor, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemAcessoFornecedores.delete()
        return redirect('/painel/')
    return render(request, "excluiAcessoFornecedores.html", {'itemAcessoFornecedores': itemAcessoFornecedores})

def excluiAcessoCarros(request, nr_item):
    print(nr_item)
    itemAcessoCarros = get_object_or_404(AcessoCarro, pk=nr_item)
    if request.method == 'POST':
        print(nr_item)
        itemAcessoCarros.delete()
        return redirect('/painel/')
    return render(request, "excluiAcessoCarros.html", {'itemAcessoCarros': itemAcessoCarros})




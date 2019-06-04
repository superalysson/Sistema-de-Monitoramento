"""SEGV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from painel.views import painel
from painel.views import adicionaCadastroVisitantes
from painel.views import listaCadastroVisitantes
from painel.views import listaCadastroMoradores
from painel.views import listaCadastroFornecedores
from painel.views import listaCadastroCarros
from painel.views import listaAcessoMoradores
from painel.views import itemCadastroVisitantes
from painel.views import atualizaCadastroVisitantes
from painel.views import atualizaCadastroMoradores
from painel.views import atualizaCadastroFornecedores
from painel.views import atualizaCadastroCarros
from painel.views import atualizaAcessoVisitante
from painel.views import atualizaAcessoMoradores
from painel.views import atualizaAcessoFornecedores
from painel.views import atualizaAcessoCarros
from painel.views import excluiCadastroVisitantes
from painel.views import excluiCadastroFornecedores
from painel.views import excluiCadastroMorador
from painel.views import excluiCadastroCarros
from painel.views import excluiAcessoMorador
from painel.views import excluiAcessoVisitantes
from painel.views import excluiAcessoFornecedores
from painel.views import excluiAcessoCarros
from painel.views import adicionaCadastroMorador
from painel.views import adicionaCadastroFornecedor
from painel.views import adicionaCadastroCarros
from painel.views import adicionaAcessoCarro
from painel.views import adicionaAcessoFornecedor
from painel.views import adicionaAcessoMoradores
from painel.views import adicionaAcessoVisitante
from painel.views import verVisitante
from painel.views import verMorador
from painel.views import verFornecedor
from painel.views import verCarros
from painel.views import suporte
from painel.views import adicionaDiario
from painel.views import listaAcessoVisitantes
from painel.views import listaAcessoFornecedores
from painel.views import listaAcessoCarros
from painel.views import listaDiario
from painel.views import atualizaDiario
from painel.views import excluiDiario
from painel.views import adicionaMensagem
from painel.views import listaMensagem
from painel.views import atualizaMensagem
from painel.views import excluiMensagem
from painel.views import login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('painel/', painel),
    path('suporte/', suporte),
    path('adicionarDiario/', adicionaDiario),
    path('adicionaMensagem/', adicionaMensagem),
    path('adicionaCadastroVisitante/', adicionaCadastroVisitantes),
    path('adicionaCadastroMorador/', adicionaCadastroMorador),
    path('adicionaCadastroCarros/', adicionaCadastroCarros),
    path('adicionaCadastroFornecedor/', adicionaCadastroFornecedor),
    path('adicionaAcessoVisitante/', adicionaAcessoVisitante),
    path('adicionaAcessoMorador/', adicionaAcessoMoradores),
    path('adicionaAcessoCarro/', adicionaAcessoCarro),
    path('adicionaAcessoFornecedor/', adicionaAcessoFornecedor),
    path('listaCadastroFornecedores/', listaCadastroFornecedores),
    path('listaCadastroVisitantes/', listaCadastroVisitantes),
    path('listaCadastroMoradores/', listaCadastroMoradores),
    path('listaCadastroCarros/', listaCadastroCarros),
    path('listaAcessoMoradores/', listaAcessoMoradores),
    path('listaAcessoCarros/', listaAcessoCarros),
    path('listaDiario/', listaDiario),
    path('listaMensagem/', listaMensagem),
    path('atualizaMensagem/<int:nr_item>/', atualizaMensagem),
    path('atualizaDiario/<int:nr_item>/', atualizaDiario),
    path('excluiDiario/<int:nr_item>/', excluiDiario),
    path('excluiMensagem/<int:nr_item>/', excluiMensagem),
    path('itemCadastroVisitantes/<int:nr_item>/', itemCadastroVisitantes),
    path('atualizaCadastroVisitantes/<int:nr_item>/', atualizaCadastroVisitantes),
    path('atualizaCadastroMoradores/<int:nr_item>/', atualizaCadastroMoradores),
    path('atualizaCadastroFornecedores/<int:nr_item>/', atualizaCadastroFornecedores),
    path('atualizaCadastroCarros/<int:nr_item>/', atualizaCadastroCarros),
    path('atualizaAcessoVisitantes/<int:nr_item>/', atualizaAcessoVisitante),
    path('atualizaAcessoCarros/<int:nr_item>/', atualizaAcessoCarros),
    path('atualizaAcessoFornecedores/<int:nr_item>/', atualizaAcessoFornecedores),
    path('atualizaAcessoMoradores/<int:nr_item>/', atualizaAcessoMoradores),
    path('excluiCadastroVisitantes/<int:nr_item>/', excluiCadastroVisitantes),
    path('excluiAcessoFornecedores/<int:nr_item>/', excluiAcessoFornecedores),
    path('excluiCadastroFornecedores/<int:nr_item>/', excluiCadastroFornecedores),
    path('excluiCadastroCarros/<int:nr_item>/', excluiCadastroCarros),
    path('excluiCadastroMorador/<int:nr_item>/', excluiCadastroMorador),
    path('excluiAcessoMorador/<int:nr_item>/', excluiAcessoMorador),
    path('excluiAcessoVisitantes/<int:nr_item>/', excluiAcessoVisitantes),
    path('excluiAcessoCarros/<int:nr_item>/', excluiAcessoCarros),
    path('verVisitante/', verVisitante),
    path('verMorador/', verMorador),
    path('verFornecedor/', verFornecedor),
    path('verCarros/', verCarros),
    path('listaAcessoVisitantes/', listaAcessoVisitantes),
    path('listaAcessoFornecedores/', listaAcessoFornecedores),


]

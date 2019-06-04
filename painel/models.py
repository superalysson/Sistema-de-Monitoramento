from django.db import models
from django.shortcuts import render





def painel(request):
    return render(request, "painel.html")


class CadastroVisitantes(models.Model):
    nomeVisitante = models.CharField(max_length=100)
    rgVisitante = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeVisitante

class CadastroFornecedores(models.Model):
    nomeFornecedor = models.CharField(max_length=100)
    rgFornecedor = models.CharField(max_length=20)
    cpfFornecedor = models.CharField(max_length=20, default="NT")
    descricaoFornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeFornecedor

class CadastroCarros(models.Model):
    placaCarro = models.CharField(max_length=10)
    modeloCarro = models.CharField(max_length=50)
    corCarro = models.CharField(max_length=100)

    def __str__(self):
        return self.placaCarro

class CadastroMorador(models.Model):
    nomeMorador = models.CharField(max_length=100)
    rgMorador = models.CharField(max_length=20)
    enderecoMorador = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeMorador

class AcessoMorador(models.Model):
    nomeMorador = models.ForeignKey(CadastroMorador, on_delete=models.CASCADE)
    dataEntrada = models.DateField()
    horaEntrada = models.TimeField()
    dataSaida = models.DateField()
    horaSaida = models.TimeField()

    def __str__(self):
        return self.nomeMorador , self.dataEntrada

class AcessoVisitante(models.Model):
    nomeVisitante = models.ForeignKey(CadastroVisitantes, on_delete=models.CASCADE)
    dataEntrada = models.DateField()
    horaEntrada = models.TimeField()
    dataSaida = models.DateField()
    horaSaida = models.TimeField()

    def __str__(self):
        return self. nomeVisitante, self.dataEntrada

class AcessoCarro(models.Model):
    placaCarro = models.ForeignKey(CadastroCarros, on_delete=models.CASCADE)
    dataEntrada = models.DateField()
    horaEntrada = models.TimeField()
    dataSaida = models.DateField()
    horaSaida = models.TimeField()

    def __str__(self):
        return self.placaCarro, self.dataEntrada

class AcessoFornecedor(models.Model):
    nomeFornecedor = models.ForeignKey(CadastroFornecedores, on_delete=models.CASCADE)
    dataEntrada = models.DateField()
    horaEntrada = models.TimeField()
    dataSaida = models.DateField()
    horaSaida = models.TimeField()

    def __str__(self):
        return self.nomeFornecedor, self.dataEntrada

class Diario(models.Model):
    autorDiario = models.CharField(max_length=100)
    dataEntrada = models.DateField()
    mensagem = models.TextField()

    def __str__(self):
        return self.dataEntrada, self.autorDiario


class Mensagem(models.Model):
    autorMensagem = models.CharField(max_length=100)
    dataEntrada = models.DateField()
    mensagem = models.CharField(max_length=200)

    def __str__(self):
        return self.dataEntrada, self.mensagem


def listaCadastroVisitantes(request):
    listaCadastroVisitantes_itens = CadastroVisitantes.objects.all()
    return render(request, "listaCadastroVisitantes.html", {'listaCadastroVisitantes_itens': listaCadastroVisitantes_itens})

def listaCadastroFornecedores(request):
    listaCadastroFornecedores_itens = CadastroFornecedores.objects.all()
    return render(request, "listaCadastroFornecedores.html", {'listaCadastroFornecedores_itens': listaCadastroFornecedores_itens})

def listaCadastroCarros(request):
    listaCadastroCarros_itens = CadastroCarros.objects.all()
    return render(request, "listaCadastroCarros.html", {'listaCadastroCarros_itens': listaCadastroCarros_itens})

def listaCadastroMoradores(request):
    listaCadastroMoradores_itens = CadastroMorador.objects.all()
    return render(request, "listaCadastroMoradores.html", {'listaCadastroMoradores_itens': listaCadastroMoradores_itens})

def listaAcessoVisitantes(request):
    listaAcessoVisitantes_itens = AcessoVisitante.objects.all()
    return render(request, "listaAcessoVisitantes.html", {'listaAcessoVisitantes_itens': listaAcessoVisitantes_itens})

def listaAcessoFornecedores(request):
    listaAcessoFornecedores_itens = AcessoFornecedor.objects.all()
    return render(request, "listaAcessoFornecedores.html", {'listaAcessoFornecedores_itens': listaAcessoFornecedores_itens})

def listaAcessoCarros(request):
    listaAcessoCarros_itens = AcessoCarro.objects.all()
    return render(request, "listaAcessoCarros.html", {'listaAcessoCarros_itens': listaAcessoCarros_itens})

def listaAcessoMoradores(request):
    listaAcessoMoradores_itens = AcessoMorador.objects.all()
    return render(request, "listaAcessoMoradores.html", {'listaAcessoMoradores_itens': listaAcessoMoradores_itens})














# Create your models here.

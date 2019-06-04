from django import forms
from painel.models import CadastroVisitantes
from painel.models import CadastroFornecedores
from painel.models import CadastroCarros
from painel.models import CadastroMorador
from painel.models import AcessoCarro
from painel.models import AcessoFornecedor
from painel.models import AcessoMorador
from painel.models import AcessoVisitante
from painel.models import Diario
from painel.models import Mensagem

class CadastroVisitanteForm(forms.ModelForm):
    class Meta:
        model = CadastroVisitantes
        fields = ('nomeVisitante', 'rgVisitante')

class CadastroFornecedoresForm(forms.ModelForm):
    class Meta:
        model = CadastroFornecedores
        fields = ('nomeFornecedor', 'rgFornecedor', 'cpfFornecedor', 'descricaoFornecedor')

class CadastroCarrosForm(forms.ModelForm):
    class Meta:
        model = CadastroCarros
        fields = ('placaCarro', 'modeloCarro', 'corCarro')

class CadastroMoradorForm(forms.ModelForm):
    class Meta:
        model = CadastroMorador
        fields = ('nomeMorador', 'rgMorador', 'enderecoMorador')

class AcessoMoradorForm(forms.ModelForm):
    class Meta:
        model = AcessoMorador
        fields = ('nomeMorador', 'dataEntrada', 'horaEntrada', 'dataSaida', 'horaSaida')

class AcessoCarroForm(forms.ModelForm):
    class Meta:
        model = AcessoCarro
        fields = ('placaCarro', 'dataEntrada', 'horaEntrada', 'dataSaida', 'horaSaida')

class AcessoFornecedorForm(forms.ModelForm):
    class Meta:
        model = AcessoFornecedor
        fields = ('nomeFornecedor', 'dataEntrada', 'horaEntrada', 'dataSaida', 'horaSaida')

class AcessoVisitanteForm(forms.ModelForm):
    class Meta:
        model = AcessoVisitante
        fields = ('nomeVisitante', 'dataEntrada', 'horaEntrada', 'dataSaida', 'horaSaida')

class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = ('autorDiario', 'dataEntrada', 'mensagem')

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ('autorMensagem', 'dataEntrada', 'mensagem')

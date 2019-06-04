from django.contrib import admin


from painel.models import CadastroMorador
from painel.models import CadastroCarros
from painel.models import CadastroFornecedores
from painel.models import CadastroVisitantes
from painel.models import AcessoVisitante
from painel.models import AcessoMorador
from painel.models import AcessoFornecedor
from painel.models import AcessoCarro


admin.site.register(CadastroVisitantes)
admin.site.register(CadastroFornecedores)
admin.site.register(CadastroCarros)
admin.site.register(CadastroMorador)
admin.site.register(AcessoCarro)
admin.site.register(AcessoFornecedor)
admin.site.register(AcessoMorador)
admin.site.register(AcessoVisitante)


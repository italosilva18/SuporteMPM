from django.forms import ModelForm
from app.models import Cadatro_Lojas

# Create the form class.
class Cadatro_LojasForm(ModelForm):
    class Meta:
        model = Cadatro_Lojas
        fields = ['RAZAO_SOCIAL', 'CNPJ', 'NOME_FANTASIA', 'RESPONSAVEL', 'VENDEDOR', 'AUTOMACAO', 'ANALISTA', 'DATA_ATIVACAO', 'STATUS']
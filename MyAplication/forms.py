from django import forms
from .models import Fornecedores

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['NomeFornecedor','EmailFornecedor']
      

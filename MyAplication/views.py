
from django.shortcuts import render,redirect
from .models import Fornecedores
from .forms import FornecedorForm

def index(request):
    return render(request, 'index.html', {})


def List_Fornecedores(request):
    forn = Fornecedores.objects.all()

    return render(request, 'Fornecedores.html', {'fornecedores': forn})  

def Criar_fornecedor(request):
    form = FornecedorForm(request.POST or None )

    if form.is_valid():
        form.save()
        return redirect('List_Fornecedores')
    
    return render(request, 'CadastrarFornecedor.html', {'form' : form})    
    pass

    
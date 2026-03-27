from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Empresa

def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('-criado_em')
    return render(request, 'empresas/listar_empresas.html', {'empresas': empresas})


def cadastrar_empresa(request):
    if request.method == 'POST':
        try:
            dados = _dados_formulário(request)
            empresa = Empresa(**dados)              

            empresa.full_clean()
            empresa.save()

            messages.success(request, "Empresa cadastrada com sucesso!")
            return redirect('empresa:listar_empresas')

        except ValidationError as e:
            context = _base_context(
                data=request.POST,
                errors=e.message_dict,
            )
            return render(request, 'empresas/cad_empresas.html', context)

        except Exception as e:
            messages.error(request, f"Erro inesperado: {str(e)}")
            context = _base_context(data=request.POST)
            return render(request, 'empresas/cad_empresas.html', context)

    return render(request, 'empresas/cad_empresas.html', _base_context())


def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST':
        try:
            dados = _dados_formulário(request)
            for key, value in dados.items():
                setattr(empresa, key, value)

            empresa.full_clean()
            empresa.save()

            messages.success(request, "Empresa atualizada com sucesso!")
            return redirect('empresa:listar_empresas')

        except ValidationError as e:
            context = _base_context(
                empresa=empresa,
                data=request.POST,
                errors=e.message_dict,
            )
            return render(request, 'empresas/cad_empresas.html', context)

        except Exception as e:
            messages.error(request, f"Erro inesperado: {str(e)}")
            context = _base_context(empresa=empresa, data=request.POST)
            return render(request, 'empresas/cad_empresas.html', context)

    context = _base_context(empresa=empresa, data=_data_de_empresa(empresa))
    return render(request, 'empresas/cad_empresas.html', context)


def excluir_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    messages.success(request, "Empresa excluída com sucesso!")
    return redirect('empresa:listar_empresas')


def _data_vazio():
    return {
        'razao_social': '',
        'nome_fantasia': '',
        'cnpj': '',
        'inscricao_estadual': '',
        'inscricao_municipal': '',
        'cnae_principal': '',
        'logradouro': '',
        'numero': '',
        'bairro': '',
        'cidade': '',
        'complemento': '',
        'estado': '',
        'cep': '',
        'pais': 'Brasil',
        'email': '',
        'telefone': '',
        'regime_tributario': '',
        'tipo_empresa': 'MATRIZ',
        'moeda_padrao': 'BRL',
        'senha_certificado': '',
        'ativo': 'on',
        'matriz': '',
    }

def _data_de_empresa(empresa):
    return {
        'razao_social': empresa.razao_social or '',
        'nome_fantasia': empresa.nome_fantasia or '',
        'cnpj': empresa.cnpj or '',
        'inscricao_estadual': empresa.inscricao_estadual or '',
        'inscricao_municipal': empresa.inscricao_municipal or '',
        'cnae_principal': empresa.cnae_principal or '',
        'logradouro': empresa.logradouro or '',
        'numero': empresa.numero or '',
        'bairro': empresa.bairro or '',
        'cidade': empresa.cidade or '',
        'complemento': empresa.complemento or '',
        'estado': empresa.estado or '',
        'cep': empresa.cep or '',
        'pais': empresa.pais or 'Brasil',
        'email': empresa.email or '',
        'telefone': empresa.telefone or '',
        'regime_tributario': empresa.regime_tributario or '',
        'tipo_empresa': empresa.tipo_empresa or 'MATRIZ',
        'moeda_padrao': empresa.moeda_padrao or 'BRL',
        'senha_certificado': empresa.senha_certificado or '',
        'ativo': 'on' if empresa.ativo else '',
        'matriz': str(empresa.matriz_id) if empresa.matriz_id else '',
    }


def _base_context(empresa=None, data=None, errors=None):
    return {
        'empresa': empresa,
        'data': data if data is not None else _data_vazio(),
        'errors': errors,
        'regimes': Empresa.REGIME_TRIBUTARIO_CHOICES,
        'tipos': Empresa.TIPO_EMPRESA_CHOICES,
        'moedas': Empresa.MOEDA_CHOICES,
        'matrizes': Empresa.objects.filter(tipo_empresa='MATRIZ'),
    }


def _dados_formulário(request):
    return {
        'razao_social': request.POST.get('razao_social'),
        'nome_fantasia': request.POST.get('nome_fantasia'),
        'cnpj': request.POST.get('cnpj'),
        'inscricao_estadual': request.POST.get('inscricao_estadual'),
        'inscricao_municipal': request.POST.get('inscricao_municipal'),
        'cnae_principal': request.POST.get('cnae_principal'),
        'logradouro': request.POST.get('logradouro'),
        'numero': request.POST.get('numero'),
        'bairro': request.POST.get('bairro'),
        'cidade': request.POST.get('cidade'),
        'complemento': request.POST.get('complemento'),
        'estado': request.POST.get('estado'),
        'cep': request.POST.get('cep'),
        'pais': request.POST.get('pais', 'Brasil'),
        'email': request.POST.get('email'),
        'telefone': request.POST.get('telefone'),
        'regime_tributario': request.POST.get('regime_tributario'),
        'tipo_empresa': request.POST.get('tipo_empresa'),
        'moeda_padrao': request.POST.get('moeda_padrao'),
        'senha_certificado': request.POST.get('senha_certificado'),
        'ativo': request.POST.get('ativo') == 'on',
        'logo': request.FILES['logo'] if request.FILES.get('logo') else None,
        'certificado_digital': request.FILES['certificado_digital'] if request.FILES.get('certificado_digital') else None,
        'matriz_id': int(request.POST.get('matriz')) if request.POST.get('matriz') else None
    }



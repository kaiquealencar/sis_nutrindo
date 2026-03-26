import pytest
from django.core.exceptions import ValidationError
from apps.empresa.models import Empresa


@pytest.mark.django_db
def test_criar_empresa():
    empresa = Empresa(
        razao_social="Empresa Teste LTDA",
        nome_fantasia="Empresa Teste",
        cnpj="52.038.391/0001-37",
        inscricao_estadual="123456789",
        inscricao_municipal="987654321",
        logradouro="Rua Teste",
        numero="123",
        complemento="Sala 1",
        bairro="Centro",
        cidade="Cidade Teste",
        estado="ST",
        cep="12345-678",
        pais="Brasil",
        logo="logo.png",
        regime_tributario="SN",
        cnae_principal="6201-5/01",
        moeda_padrao="BRL",
        certificado_digital="certificado.pfx",
        senha_certificado="senha123",
        telefone="(11) 1234-5678",
        email="example@example.com.br"
    )
    
    empresa.full_clean()
    empresa.save()

    assert Empresa.objects.count() == 1
    e = Empresa.objects.get()

    assert e.razao_social == "Empresa Teste LTDA"
    assert e.nome_fantasia == "Empresa Teste"
    assert e.cnpj == "52038391000137"


@pytest.mark.django_db
def test_editar_empresa():
    empresa = Empresa.objects.create(
        razao_social="Empresa Teste LTDA",
        nome_fantasia="Empresa Teste",
        cnpj="52.038.391/0001-37",
        inscricao_estadual="123456789",
        inscricao_municipal="987654321",
        logradouro="Rua Teste",
        numero="123",
        complemento="Sala 1",
        bairro="Centro",
        cidade="Cidade Teste",
        estado="ST",
        cep="12345-678",
        pais="Brasil",
        logo="logo.png",
        regime_tributario="SN",
        cnae_principal="6201-5/01",
        moeda_padrao="BRL",
        certificado_digital="certificado.pfx",
        senha_certificado="senha123",
        telefone="(11) 1234-5678",
        email="example@example.com.br"
    )
    empresa.razao_social = "Empresa Editada LTDA"
    empresa.full_clean()
    empresa.save()

    empresa_atualizada = Empresa.objects.get(id=empresa.id)
    assert empresa_atualizada.razao_social == "Empresa Editada LTDA"

@pytest.mark.django_db
def test_excluir_empresa():
    empresa = Empresa.objects.create(
        razao_social="Empresa Teste LTDA",
        nome_fantasia="Empresa Teste",
        cnpj="52.038.391/0001-37",
        inscricao_estadual="123456789",
        inscricao_municipal="987654321",
        logradouro="Rua Teste",
        numero="123",
        complemento="Sala 1",
        bairro="Centro",
        cidade="Cidade Teste",
        estado="ST",
        cep="12345-678",
        pais="Brasil",
        logo="logo.png",
        regime_tributario="SN",
        cnae_principal="6201-5/01",
        moeda_padrao="BRL",
        certificado_digital="certificado.pfx",
        senha_certificado="senha123",
        telefone="(11) 1234-5678",
        email="example@example.com.br"
    )       
    empresa.delete()
    assert Empresa.objects.count() == 0
    
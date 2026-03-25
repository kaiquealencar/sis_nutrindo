import pytest
from django.urls import reverse 
from apps.usuarios.models import Usuario


@pytest.mark.django_db
def test_listar_usuarios(client):
    Usuario.objects.create_user(
        email="example@example.com.br",
        nome="fulano",
        password="senha123",
        role="admin"
    )

    response = client.get(reverse("usuarios:lista_usuarios"))
    assert response.status_code == 200
    assert len(response.context["usuarios"]) == 1

@pytest.mark.django_db
def test_cadastrar_usuario(client):
    data = {
        "email": "example@example.com.br",
        "nome": "fulano",
        "password": "senha123",
        "role": "admin"
    }

    response = client.post(reverse("usuarios:cadastrar_usuario"), data=data)
    assert response.status_code == 302  
    assert Usuario.objects.count() == 1

@pytest.mark.django_db
def test_editar_usuario(client):
    usuario = Usuario.objects.create_user(
        email="example@example.com.br",
        nome="fulano",
        password="senha123",
        role="admin"
    )

    data = {
        "email": "updated@example.com.br",
        "nome": "ciclano",
        "password": "nova_senha123",
        "role": "user"
    }

    response = client.post(reverse("usuarios:editar_usuario", kwargs={"id": usuario.id}), data=data)
    assert response.status_code == 302
    usuario.refresh_from_db()
    assert usuario.email == data["email"]
    assert usuario.nome == data["nome"]
    assert usuario.role == data["role"]

@pytest.mark.django_db
def test_excluir_usuario(client):
    usuario = Usuario.objects.create_user(
        email="example@example.com.br",
        nome="fulano",
        password="senha123",
        role="admin"
    )

    response = client.post(reverse("usuarios:excluir_usuario", kwargs={"id": usuario.id}))
    assert response.status_code == 302
    assert Usuario.objects.count() == 0
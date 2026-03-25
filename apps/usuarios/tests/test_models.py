import pytest 
from django.core.exceptions import ValidationError
from apps.usuarios.models import Usuario


@pytest.mark.django_db
def test_criar_usuario():
    usuario = Usuario.objects.create_user(
        email="example@example.com.br",
        nome="fulano",
        password="senha123",
        role="admin"
    )
     
    usuario.full_clean()    
    usuario.save()

    u = Usuario.objects.first()

    assert u.email == "example@example.com.br"
    assert u.nome == "fulano"
    assert u.role == "admin"
    assert u.check_password("senha123") 
    
@pytest.mark.django_db
def test_editar_usuario():
    usuario = Usuario.objects.create_user(
        email="example@example",
        nome="fulano",
        password="senha123",
        role="admin"
    )

    usuario.email = "email_edit@example.com"
    usuario.full_clean()
    usuario.save()

    usuario_atualizado = Usuario.objects.get(nome="fulano")

    assert usuario_atualizado.email == "email_edit@example.com"

@pytest.mark.django_db
def test_excluir_usuario():
    usuario = Usuario.objects.create_user(
        email="example@example",
        nome="fulano",
        password="senha123",
        role="admin"
    )

    usuario.delete()

    assert Usuario.objects.count() == 0 
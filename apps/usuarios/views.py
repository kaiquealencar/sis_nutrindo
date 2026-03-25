from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario


def cad_usuario(request):
    if request.method == 'POST':
        usuario_data = {
            "email": request.POST.get("email"),
            "nome": request.POST.get("nome"),
            "password": request.POST.get("password"),
            "role": request.POST.get("role")
        }

        Usuario.objects.create_user(**usuario_data)

        messages.success(request, f"Usuário: {usuario_data['email']} cadastrado com sucesso!")
        return redirect('lista_usuarios')

    return render(request, 'usuarios/cad_usuario.html')



def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})



def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        usuario.email = request.POST.get("email")
        usuario.nome = request.POST.get("nome")
        password = request.POST.get("password")
        ativo = request.POST.get("is_active") == 'on'
        if password:
            usuario.set_password(password) 
        usuario.role = request.POST.get("role")
        usuario.is_active = ativo

        usuario.save()

        messages.success(request, f"Usuário {usuario.email} atualizado com sucesso!")
        return redirect('lista_usuarios')

    return render(request, 'usuarios/cad_usuario.html', {'usuario': usuario})


def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, f"Usuário {usuario.email} excluído com sucesso!")
    return redirect('lista_usuarios')
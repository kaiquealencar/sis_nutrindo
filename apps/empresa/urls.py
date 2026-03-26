from django.urls import path
from .views import listar_empresas, cadastrar_empresa, editar_empresa, excluir_empresa

app_name = 'empresa'

urlpatterns = [
    path('', listar_empresas, name='listar_empresas'),
    path('cadastrar/', cadastrar_empresa, name='cadastrar_empresa'),
    path('editar/<int:id>/', editar_empresa, name='editar_empresa'),
    path('excluir/<int:id>/', excluir_empresa, name='excluir_empresa')
]



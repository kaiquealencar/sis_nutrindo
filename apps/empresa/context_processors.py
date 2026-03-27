from .models import Empresa
from django.conf import settings



def empresa_context(request):
    empresa = Empresa.objects.filter(tipo_empresa="MATRIZ", ativo=True).order_by("id").first()
    
    return {
        "empresa": empresa,
        "GLOBAL_SYSTEM_NAME": settings.GLOBAL_SYSTEM_NAME
    }
    
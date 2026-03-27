from .models import Empresa

def empresa_context(request):
    empresa = Empresa.objects.filter(tipo_empresa='MATRIZ', ativo=True).order_by('id').first()
    
    return {
        'empresa': empresa
    }
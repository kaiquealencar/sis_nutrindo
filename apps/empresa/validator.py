import re
from django.core.exceptions import ValidationError


def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14:
        raise ValidationError('CNPJ deve conter 14 dígitos.')

    if cnpj == cnpj[0] * 14:
        raise ValidationError('CNPJ inválido.')

    def calcular_digito(cnpj, peso):
        soma = sum(int(digito) * peso[i] for i, digito in enumerate(cnpj))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    peso1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    peso2 = [6] + peso1

    digito1 = calcular_digito(cnpj[:12], peso1)
    digito2 = calcular_digito(cnpj[:12] + digito1, peso2)

    if cnpj[-2:] != digito1 + digito2:
        raise ValidationError('CNPJ inválido.')
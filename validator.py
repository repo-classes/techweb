# documentos.py
import re
from typing import Optional

def _limpar_documento(doc: str) -> str:
    return re.sub(r'\D', '', doc.strip())

def validar_cpf(cpf: str) -> bool:
    cpf = _limpar_documento(cpf)
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito1:
        return False

    # Segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito2:
        return False

    return True


def validar_cnpj(cnpj: str) -> bool:
    cnpj = _limpar_documento(cnpj)

    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False

    # Primeiro dígito verificador
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cnpj[12]) != digito1:
        return False

    # Segundo dígito verificador
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cnpj[13]) != digito2:
        return False

    return True
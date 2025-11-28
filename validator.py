import re
from typing import Optional

def validate_cpf(cpf: str) -> bool:

    cpf = re.sub(r'\D', '', cpf.strip())

    if len(cpf) != 11 or len(set(cpf)) == 1: return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito1: return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito2: return False

    return True
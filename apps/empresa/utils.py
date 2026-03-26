import re

def somente_numeros(value: str | None) -> str:    
    return re.sub(r'\D', '', value or '')
import re

def extract_data_from_text(text):
    data = {
        "Orgão": extract_orgao(text),
        "CNPJ": extract_cnpj(text),
        "Cidade": extract_cidade(text),
        "Estado": extract_estado(text),
        "Email": extract_email(text),
        "Telefone": extract_telefone(text),
        "Prazo de Pagamento": extract_prazo_pagamento(text),
        "Prazo de Entrega": extract_prazo_entrega(text),
        "Validade da Proposta": extract_validade_proposta(text),
        "Local de Entrega": extract_local_entrega(text)
    }
    return data

def extract_orgao(text):
    patterns = [
        r"Órgão\s*:\s*([^\n]+)",
        r"Secretaria\s*:\s*([^\n]+)",
        r"(?:Poder|Governo)\s*:\s*([^\n]+)"
    ]
    return try_patterns(text, patterns)

def extract_cnpj(text):
    patterns = [
        r"CNPJ\s*:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})",
        r"(\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b)"
    ]
    return try_patterns(text, patterns)

def extract_cidade(text):
    patterns = [
        r"Município\s*:\s*([^\n,]+)",
        r"Cidade\s*:\s*([^\n,]+)"
    ]
    return try_patterns(text, patterns)

def extract_estado(text):
    patterns = [
        r"UF\s*:\s*([A-Z]{2})",
        r"Estado\s*:\s*([^\n,]+)"
    ]
    return try_patterns(text, patterns)

def extract_email(text):
    patterns = [
        r"E[-\s]*mail\s*:\s*([^\s@]+@[^\s@]+\.[^\s@]+)",
        r"([\w.-]+@[\w.-]+\.\w+)"
    ]
    return try_patterns(text, patterns)

def extract_telefone(text):
    patterns = [
        r"Telefone\s*:\s*([\d\s\(\)-]+)",
        r"Contato\s*:\s*([\d\s\(\)-]+)"
    ]
    return try_patterns(text, patterns)

def extract_prazo_pagamento(text):
    patterns = [
        r"Prazo\s*de\s*Pagamento\s*:\s*([^\n]+)",
        r"Condições\s*de\s*pagamento\s*:\s*([^\n]+)"
    ]
    return try_patterns(text, patterns)

def extract_prazo_entrega(text):
    patterns = [
        r"Prazo\s*de\s*Entrega\s*:\s*([^\n]+)",
        r"Entrega\s*:\s*([^\n]+)"
    ]
    return try_patterns(text, patterns)

def extract_validade_proposta(text):
    patterns = [
        r"Validade\s*da\s*Proposta\s*:\s*([^\n]+)",
        r"Proposta\s*válida\s*até\s*:\s*([^\n]+)"
    ]
    return try_patterns(text, patterns)

def extract_local_entrega(text):
    patterns = [
        r"Local\s*de\s*Entrega\s*:\s*([^\n]+)",
        r"Endereço\s*para\s*entrega\s*:\s*([^\n]+)"
    ]
    return try_patterns(text, patterns)

def try_patterns(text, patterns):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return "N/A"
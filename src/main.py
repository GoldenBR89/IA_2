import os
import pandas as pd
from src.extractors import extract_data_from_text
from src.utils import setup_directories, log_processed_file, is_file_processed

def process_editais():
    setup_directories()
    data_dir = "data"
    output_file = "outputs/dados_editais.xlsx"

    # Carrega dados existentes
    try:
        df = pd.read_excel(output_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "Arquivo", "Orgão", "CNPJ", "Cidade", "Estado",
            "Email", "Telefone", "Prazo de Pagamento",
            "Prazo de Entrega", "Validade da Proposta", "Local de Entrega"
        ])

    # Processa cada PDF
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf") and not is_file_processed(filename):
            print(f"\n🔍 Processando: {filename}")
            pdf_path = os.path.join(data_dir, filename)
            
            # Extrai texto do PDF
            text = extract_text_from_pdf(pdf_path)
            if not text.strip():
                print(f"❌ ERRO: O arquivo {filename} está vazio ou não pode ser lido.")
                continue
            
            # Extrai dados
            data = extract_data_from_text(text)
            data["Arquivo"] = filename  # Adiciona nome do arquivo
            
            # Valida campos críticos
            if data["CNPJ"] == "N/A":
                print(f"⚠️ Aviso: CNPJ não encontrado em {filename}")
            if data["Orgão"] == "N/A":
                print(f"⚠️ Aviso: Órgão não encontrado em {filename}")
            
            # Adiciona à planilha
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
            log_processed_file(filename)
            
            # Mostra dados extraídos
            print("✅ Dados Capturados:")
            for key, value in data.items():
                print(f"- {key}: {value}")

    # Salva planilha
    df.to_excel(output_file, index=False)
    print(f"\n📊 Planilha atualizada: {output_file}")

def extract_text_from_pdf(pdf_path):
    import pdfplumber
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"❌ Erro ao processar PDF {pdf_path}: {str(e)}")
    return text

if __name__ == "__main__":
    process_editais()
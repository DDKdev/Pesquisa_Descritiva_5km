import re
import pandas as pd

# 1. Ler o arquivo de texto original
with open('dados_corrida.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

atletas = []
i = 0
total_linhas = len(linhas)

while i < total_linhas:
    linha_atual = linhas[i].strip()
    
    # Identifica se a linha é uma posição (ex: '1º', '2º', etc.)
    if re.match(r'^\d+º$', linha_atual):
        posicao = linha_atual
        sexo = linhas[i+1].strip() if i+1 < total_linhas else ""
        
        # A linha seguinte (i+2) contém: Nome \t Peito \t Categoria \t Tempo Bruto
        dados_principais = linhas[i+2].strip() if i+2 < total_linhas else ""
        partes = dados_principais.split("\t")
        
        nome = partes[0] if len(partes) > 0 else ""
        peito = partes[1] if len(partes) > 1 else ""
        categoria = partes[2] if len(partes) > 2 else ""
        tempo_bruto = partes[3] if len(partes) > 3 else ""
        
        # Próximas linhas podem conter o tempo líquido e o pace
        tempo_liquido = ""
        ritmo = ""
        
        # Olha adiante para ver se encontra 'líq.' ou '/km'
        for offset in [3, 4, 5]:
            if i + offset < total_linhas:
                prox_linha = linhas[i + offset].strip()
                if "líq." in prox_linha:
                    tempo_liquido = prox_linha.replace("líq.", "").strip()
                elif "/km" in prox_linha:
                    ritmo = prox_linha.strip()

        atletas.append({
            "Posicao": posicao,
            "Sexo": sexo,
            "Nome": nome,
            "Peito": peito,
            "Categoria": categoria,
            "Tempo_Bruto": tempo_bruto,
            "Tempo_Liquido": tempo_liquido,
            "Pace": ritmo,
            "Status": "Concluiu"
        })
    
    # Trata atletas sem tempo ou desqualificados (começam com '—')
    elif linha_atual.startswith("—"):
        partes = linha_atual.split("\t")
        nome = partes[1] if len(partes) > 1 else ""
        peito = partes[2] if len(partes) > 2 else ""
        categoria = partes[3] if len(partes) > 3 else ""
        status = "DSQ" if "DSQ" in linha_atual else "Sem Tempo / DNS"

        atletas.append({
            "Posicao": "—",
            "Sexo": categoria[0] if categoria else "",
            "Nome": nome,
            "Peito": peito,
            "Categoria": categoria,
            "Tempo_Bruto": "",
            "Tempo_Liquido": "",
            "Pace": "",
            "Status": status
        })
        
    i += 1

# 2. Converter para DataFrame do Pandas e salvar
df_atletas = pd.DataFrame(atletas)
df_atletas.to_csv('atletas_corrida_correto.csv', index=False, encoding='utf-8-sig', sep=';')

print(f"Sucesso! {len(df_atletas)} atletas processados corretamente.")
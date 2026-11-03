import re
import pandas as pd

# 1. Ler o arquivo de texto original
with open('dados_corrida.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

atletas = []
i = 0
total_linhas = len(linhas)
id_counter = 1
id_prova = "PROVA_01"  # Altere para a identificação da prova atual (ex: P01, P02...)

while i < total_linhas:
    linha_atual = linhas[i].strip()
    
    # Identifica atletas que concluíram (posição ex: '1º', '2º')
    if re.match(r'^\d+º$', linha_atual):
        posicao = linha_atual.replace('º', '')
        sexo = linhas[i+1].strip() if i+1 < total_linhas else ""
        dados_principais = linhas[i+2].strip() if i+2 < total_linhas else ""
        partes = dados_principais.split("\t")
        
        categoria = partes[2] if len(partes) > 2 else ""
        tempo_bruto = partes[3] if len(partes) > 3 else ""
        
        # Procura pelo tempo líquido nas linhas seguintes
        tempo_liquido = ""
        for offset in [3, 4, 5]:
            if i + offset < total_linhas:
                prox_linha = linhas[i + offset].strip()
                if "líq." in prox_linha:
                    tempo_liquido = prox_linha.replace("líq.", "").strip()

        # Caso não haja tempo líquido destacado, adota o tempo bruto
        if not tempo_liquido:
            tempo_liquido = tempo_bruto

        atletas.append({
            "ID": id_counter,
            "ID_prova": id_prova,
            "Posicao": posicao,
            "Sexo": sexo,
            "Categoria": categoria,
            "Tempo_Liquido": tempo_liquido
        })
        id_counter += 1

    # Trata atletas sem tempo, ausentes ou desqualificados
    elif linha_atual.startswith("—"):
        partes = linha_atual.split("\t")
        categoria = partes[3] if len(partes) > 3 else ""
        
        atletas.append({
            "ID": id_counter,
            "ID_prova": id_prova,
            "Posicao": "—",
            "Sexo": categoria[0] if categoria else "",
            "Categoria": categoria,
            "Tempo_Liquido": ""
        })
        id_counter += 1
        
    i += 1

# 2. Converter para DataFrame e exportar para CSV
df_enxuto = pd.DataFrame(atletas)
df_enxuto.to_csv('fonte_dados_5km_enxuta.csv', index=False, encoding='utf-8-sig', sep=';')

print(f"Sucesso! {len(df_enxuto)} registros salvos com a estrutura enxuta.")
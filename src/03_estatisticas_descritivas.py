import pandas as pd
import numpy as np

# 1. Carregar a base de dados tratada (caminho relativo a partir da raiz do projeto)
CAMINHO_ARQUIVO = 'dados/processed/02_fonte_dados_5km_enxuta.csv'
df = pd.read_csv(CAMINHO_ARQUIVO, sep=None, engine='python', encoding='utf-8-sig')

print(f"Total de registros carregados: {len(df)}")
print(f"Colunas disponíveis: {df.columns.tolist()}\n")


def tempo_para_minutos(tempo_str):
    """Converte 'HH:MM:SS' (ou 'MM:SS') em minutos decimais."""
    if pd.isna(tempo_str):
        return np.nan
    partes = str(tempo_str).strip().split(':')
    if len(partes) == 3:
        h, m, s = map(float, partes)
        return h * 60 + m + s / 60
    elif len(partes) == 2:
        m, s = map(float, partes)
        return m + s / 60
    return np.nan


# Coluna auxiliar em minutos (registros sem tempo viram NaN e saem dos cálculos)
df['Tempo_Minutos'] = df['Tempo_Liquido'].apply(tempo_para_minutos)

# 2. Estatísticas descritivas
# Os concluintes formam a POPULAÇÃO da prova (censo), por isso variância
# e desvio padrão usam divisor N (ddof=0), e não n-1 (estimador amostral).
def calcular_estatisticas(subset, nome_grupo):
    dados = subset['Tempo_Minutos'].dropna()
    desvio = dados.std(ddof=0)

    return {
        'Grupo': nome_grupo,
        'N (População)': len(dados),
        'Mínimo (min)': dados.min(),
        'Máximo (min)': dados.max(),
        'Amplitude (min)': dados.max() - dados.min(),
        'Média (min)': dados.mean(),
        'Mediana (min)': dados.median(),
        'Q1 (25%)': dados.quantile(0.25),
        'Q3 (75%)': dados.quantile(0.75),
        'IQR (Q3-Q1)': dados.quantile(0.75) - dados.quantile(0.25),
        'Variância (σ²)': dados.var(ddof=0),
        'Desvio Padrão (σ)': desvio,
        'Coeficiente de Variação (%)': (desvio / dados.mean()) * 100,
    }


estatisticas_geral = calcular_estatisticas(df, "População Geral")
estatisticas_masculino = calcular_estatisticas(df[df['Sexo'] == 'M'], "Masculino (M)")
estatisticas_feminino = calcular_estatisticas(df[df['Sexo'] == 'F'], "Feminino (F)")

df_resumo = pd.DataFrame([estatisticas_geral, estatisticas_masculino, estatisticas_feminino])

print("=== RELATÓRIO DE ESTATÍSTICAS DESCRITIVAS (TEMPO LÍQUIDO) ===")
print(df_resumo.to_string(index=False, formatters={
    'Mínimo (min)': '{:.2f}'.format,
    'Máximo (min)': '{:.2f}'.format,
    'Amplitude (min)': '{:.2f}'.format,
    'Média (min)': '{:.2f}'.format,
    'Mediana (min)': '{:.2f}'.format,
    'Q1 (25%)': '{:.2f}'.format,
    'Q3 (75%)': '{:.2f}'.format,
    'IQR (Q3-Q1)': '{:.2f}'.format,
    'Variância (σ²)': '{:.2f}'.format,
    'Desvio Padrão (σ)': '{:.2f}'.format,
    'Coeficiente de Variação (%)': '{:.2f}%'.format,
}))

# 3. Exportar o resultado para CSV na pasta processed
CAMINHO_SAIDA = 'dados/processed/03_estatisticas_descritivas.csv'
df_resumo.to_csv(CAMINHO_SAIDA, index=False, encoding='utf-8-sig')
print(f"\n[Sucesso] Arquivo salvo em: {CAMINHO_SAIDA}")
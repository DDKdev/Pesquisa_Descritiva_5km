import pandas as pd
import numpy as np
import os

def analisar_por_genero():
    # 1. Carregar a base de dados tratada
    caminho = 'dados/processed/02_fonte_dados_5km_enxuta.csv'
    df = pd.read_csv(caminho, sep=None, engine='python', encoding='utf-8-sig')
    
    print(f"Total de registros carregados: {len(df)}")
    
    # 2. Conversão segura de tempo (HH:MM:SS para Minutos Decimais)
    df['Tempo_Liquido'] = pd.to_timedelta(df['Tempo_Liquido'].astype(str)).dt.total_seconds() / 60.0
    
    # Remover nulos da coluna de tempo e gênero
    df_analise = df.dropna(subset=['Tempo_Liquido', 'Sexo']).copy()
    
    print(genres := df_analise['Sexo'].unique())
    print(f"\nGêneros encontrados na base: {list(genres)}")
    
    # 3. Calcular Estatísticas Descritivas Segmentadas por Gênero
    resumo_genero = df_analise.groupby('Sexo')['Tempo_Liquido'].agg(
        Total_Atletas='count',
        Media_Min=lambda x: round(x.mean(), 2),
        Mediana_Min=lambda x: round(x.median(), 2),
        Desvio_Padrao=lambda x: round(x.std(), 2),
        Minimo=lambda x: round(x.min(), 2),
        Maximo=lambda x: round(x.max(), 2)
    ).reset_index()
    
    print("\n=== ESTATÍSTICAS DESCRITIVAS POR GÊNERO ===")
    print(resumo_genero.to_string(index=False))
    
    # Garantir que a pasta de destino existe
    os.makedirs('dados/processed', exist_ok=True)
    
    # 4. Guardar o resultado consolidado em CSV
    caminho_saida = 'dados/processed/06_estatisticas_por_genero.csv'
    resumo_genero.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print(f"\nTabela consolidada por gênero guardada com sucesso em: {caminho_saida}")

if __name__ == "__main__":
    analisar_por_genero()
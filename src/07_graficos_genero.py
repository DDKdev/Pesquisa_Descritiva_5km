import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_graficos_genero():
    # 1. Carregar a base de dados tratada
    caminho = 'dados/processed/02_fonte_dados_5km_enxuta.csv'
    df = pd.read_csv(caminho, sep=None, engine='python', encoding='utf-8-sig')
    
    print(f"Total de registros carregados para os gráficos: {len(df)}")
    
    # 2. Conversão segura de tempo (HH:MM:SS para Minutos Decimais)
    df['Tempo_Liquido'] = pd.to_timedelta(df['Tempo_Liquido'].astype(str)).dt.total_seconds() / 60.0
    
    # Remover nulos de tempo e gênero
    df_analise = df.dropna(subset=['Tempo_Liquido', 'Sexo']).copy()
    
    # Garantir que a pasta de salvamento existe
    os.makedirs('dados/processed', exist_ok=True)
    
    # Configurar o estilo visual do Seaborn
    sns.set_theme(style="whitegrid")
    
    # ==========================================
    # GRÁFICO 1: Boxplot Comparativo por Gênero
    # ==========================================
    plt.figure(figsize=(9, 6))
    sns.boxplot(
        x='Sexo', 
        y='Tempo_Liquido', 
        data=df_analise, 
        palette={'M': 'royalblue', 'F': 'orchid'},
        width=0.4
    )
    
    plt.title('Comparativo de Tempos Líquidos por Gênero (Boxplot)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Gênero', fontsize=11)
    plt.ylabel('Tempo Líquido (minutos)', fontsize=11)
    plt.tight_layout()
    
    caminho_box = 'dados/processed/grafico_03_boxplot_genero.png'
    plt.savefig(caminho_box, dpi=300)
    plt.close()
    print(f"[Sucesso] Boxplot salvo em: {caminho_box}")
    
    # ==========================================
    # GRÁFICO 2: Distribuição de Densidade Sobreposta
    # ==========================================
    plt.figure(figsize=(11, 6))
    sns.histplot(
        data=df_analise, 
        x='Tempo_Liquido', 
        hue='Sexo', 
        kde=True, 
        element='step', 
        stat='density', 
        common_norm=False,
        palette={'M': 'royalblue', 'F': 'orchid'},
        alpha=0.4
    )
    
    plt.title('Distribuição de Densidade dos Tempos por Gênero (Masculino vs Feminino)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Tempo Líquido (minutos)', fontsize=11)
    plt.ylabel('Densidade', fontsize=11)
    plt.tight_layout()
    
    caminho_densidade = 'dados/processed/grafico_04_densidade_genero.png'
    plt.savefig(caminho_densidade, dpi=300)
    plt.close()
    print(f"[Sucesso] Gráfico de densidade salvo em: {caminho_densidade}")

if __name__ == "__main__":
    gerar_graficos_genero()
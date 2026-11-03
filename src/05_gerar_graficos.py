import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_visualizacoes():
    # 1. Carregar a base de dados tratada
    caminho = 'dados/processed/02_fonte_dados_5km_enxuta.csv'
    df = pd.read_csv(caminho, sep=None, engine='python', encoding='utf-8-sig')
    
    print(f"Total de registros carregados para os gráficos: {len(df)}")
    
    # 2. Conversão segura de tempo (HH:MM:SS para Minutos Decimais)
    df['Tempo_Liquido'] = pd.to_timedelta(df['Tempo_Liquido'].astype(str)).dt.total_seconds() / 60.0
    tempos = df['Tempo_Liquido'].dropna()
    
    # Garantir que a pasta de salvamento existe
    os.makedirs('dados/processed', exist_ok=True)
    
    # Configurar o estilo visual do Seaborn para padrão profissional/acadêmico
    sns.set_theme(style="whitegrid")
    
    # ==========================================
    # GRÁFICO 1: Histograma com Curva de Densidade
    # ==========================================
    plt.figure(figsize=(10, 6))
    n = len(tempos)
    k = int(np.round(1 + 3.322 * np.log10(n))) # Regra de Sturges para número de classes
    
    sns.histplot(
        tempos, 
        bins=k, 
        kde=True, 
        color='royalblue', 
        edgecolor='black', 
        alpha=0.6
    )
    
    plt.title('Distribuição dos Tempos Líquidos - Prova 5km (População Geral)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Tempo Líquido (minutos)', fontsize=11)
    plt.ylabel('Frequência Absoluta', fontsize=11)
    plt.tight_layout()
    
    caminho_hist = 'dados/processed/grafico_geral_01_histograma.png'
    plt.savefig(caminho_hist, dpi=300)
    plt.close()
    print(f"[Sucesso] Histograma salvo em: {caminho_hist}")
    
    # ==========================================
    # GRÁFICO 2: Ogiva (Frequência Acumulada)
    # ==========================================
    counts, bin_edges = np.histogram(tempos, bins=k)
    cum_counts = np.insert(np.cumsum(counts), 0, 0) # Adiciona 0 no início para ancorar no eixo X
    
    plt.figure(figsize=(10, 6))
    plt.plot(
        bin_edges, 
        cum_counts, 
        marker='o', 
        linestyle='-', 
        color='darkorange', 
        linewidth=2.5, 
        markersize=6
    )
    
    plt.title('Ogiva de Galton (Frequência Acumulada) - Prova 5km', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Limites Superior das Classes (minutos)', fontsize=11)
    plt.ylabel('Frequência Acumulada (Fi)', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    caminho_ogiva = 'dados/processed/grafico_geral_02_ogiva.png'
    plt.savefig(caminho_ogiva, dpi=300)
    plt.close()
    print(f"[Sucesso] Ogiva acumulada salva em: {caminho_ogiva}")

if __name__ == "__main__":
    gerar_visualizacoes()
import pandas as pd
import numpy as np

def gerar_tabela_frequencias():
    # 1. Carregar a base de dados tratada (com encoding utf-8-sig para ignorar o BOM)
    caminho = 'dados/processed/02_fonte_dados_5km_enxuta.csv'
    df = pd.read_csv(caminho, sep=None, engine='python', encoding='utf-8-sig')
    
    print(f"Total de registros carregados: {len(df)}")
    
    # CONVERSÃO DE TEMPO (HH:MM:SS para Minutos Decimais)
    # pd.to_timedelta converte o formato de horas em objeto temporal e calculamos o total em minutos
    df['Tempo_Liquido'] = pd.to_timedelta(df['Tempo_Liquido'].astype(str)).dt.total_seconds() / 60.0
    
    tempos = df['Tempo_Liquido'].dropna()
    print(f"Total de registros válidos para análise: {len(tempos)}")
    
    if len(tempos) == 0:
        raise ValueError("Atenção: Nenhum valor válido foi encontrado após a conversão de tempo.")
    
    # 2. Definir parâmetros para a construção das classes usando a Regra de Sturges
    n = len(tempos)
    k = int(np.round(1 + 3.322 * np.log10(n)))
    print(f"Número de classes calculado (Sturges): {k}")
    
    # 3. Criar as classes (intervalos) usando pd.cut
    categorias = pd.cut(tempos, bins=k, right=True)
    
    # 4. Calcular Frequência Absoluta (fi)
    fa = categorias.value_counts().sort_index()
    
    # 5. Calcular Frequência Relativa (fri em %)
    fr = (fa / n) * 100
    
    # 6. Calcular Frequência Acumulada (Fi)
    Fi = fa.cumsum()
    
    # 7. Montar o DataFrame consolidado da Tabela de Frequências
    tabela_freq = pd.DataFrame({
        'Classe (Intervalo min)': [str(intervalo) for intervalo in fa.index],
        'Freq. Absoluta (fi)': fa.values,
        'Freq. Relativa (%)': fr.values.round(2),
        'Freq. Acumulada (Fi)': Fi.values
    })
    
    print("\n=== TABELA DE FREQUÊNCIAS (POPULAÇÃO GERAL) ===")
    print(tabela_freq.to_string(index=False))
    
    # Salvar a tabela gerada na pasta processed para documentação
    tabela_freq.to_csv('dados/processed/03_tabela_frequencias_geral.csv', index=False, encoding='utf-8-sig')
    print("\nTabela de frequências salva com sucesso em 'dados/processed/03_tabela_frequencias_geral.csv'!")

if __name__ == "__main__":
    gerar_tabela_frequencias()
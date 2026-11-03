import pandas as pd
import numpy as np

def gerar_base_sintetica(n_registros=1200, arquivo_saida='dados/processed/dados_sinteticos_5km.csv'):
    np.random.seed(42)
    sexos = np.random.choice(['M', 'F'], size=n_registros, p=[0.52, 0.48])
    tempos = []
    for s in sexos:
        if s == 'M':
            t = np.random.gamma(shape=12, scale=3) # Média ~36 min
        else:
            t = np.random.gamma(shape=14, scale=3.1) # Média ~43 min
        tempos.append(max(18.0, round(t, 2)))

    df = pd.DataFrame({
        'ID': range(1, n_registros + 1),
        'Sexo': sexos,
        'Tempo_Liquido_Min': tempos
    })
    df.to_csv(arquivo_saida, index=False)
    print(f'Base sintética gerada com sucesso: {arquivo_saida}')

if __name__ == '__main__':
    gerar_base_sintetica()
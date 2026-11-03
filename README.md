# 🏃‍♂️ Análise Estatística Descritiva: Prova de Corrida de 5km

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-blueviolet.svg)](https://seaborn.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto consiste em um estudo completo de **Estatística Descritiva** aplicado aos dados de tempo líquido e participação de uma prova de corrida de rua de 5 km. O objetivo é transformar dados brutos em inteligência estatística e visual para tomada de decisão em gestão de eventos esportivos e acompanhamento de desempenho.

A metodologia adota os preceitos do modelo conceitual de análise estatística da **Enap (Escola Nacional de Administração Pública)**, aplicando tratamento defensivo de dados, tabelas de frequências categorizadas via **Regra de Sturges** e segmentação por gênero.

---

## 🛠️ Arquitetura do Projeto

A estrutura do projeto adota modularização estrita (`src/`), segregação de dados em camadas de maturidade (`raw/` e `processed/`) e versionamento defensivo:

```text
5KM_PESQUISA_DESCRITIVA/
├── .vscode/                 # Configurações do ambiente de desenvolvimento (VS Code)
├── dados/
│   ├── processed/           # Dados higienizados (.csv) e gráficos exportados (.png)
│   │   ├── 01_atletas_corrida_correto.csv
│   │   ├── 02_fonte_dados_5km_enxuta.csv
│   │   ├── 03_estatisticas_descritivas.csv
│   │   ├── 03_tabela_frequencias_geral.csv
│   │   ├── 06_estatisticas_por_genero.csv
│   │   ├── dados_sinteticos_5km.csv
│   │   ├── grafico_03_boxplot_genero.png
│   │   ├── grafico_04_densidade_genero.png
│   │   ├── grafico_geral_01_histograma.png
│   │   └── grafico_geral_02_ogiva.png
│   └── raw/                 # [Local apenas] Dado bruto intocável (Omitido no Git por LGPD)
│       └── 00_dados_corrida.txt
├── docs/                    # Documentação técnica e diário de bordo
│   └── diario_de_bordo.txt
├── provas/                  # Materiais e referências de apoio
│   └── provas.txt
├── src/                     # Pipeline de scripts Python modularizados (01 a 07)
│   ├── 01_analise_dados.py
│   ├── 02_filtro_de_dados.py
│   ├── 03_estatisticas_descritivas.py
│   ├── 04_tabela_frequencias.py
│   ├── 05_gerar_graficos.py
│   ├── 06_segmentacao_genero.py
│   ├── 07_graficos_genero.py
│   └── script_ficticio.py
├── venv/                    # [Local apenas] Ambiente virtual Python (Ignorado via .gitignore)
├── .gitignore               # Regras de exclusão de arquivos para controle de versão Git
├── Documentação Técnica Completa - Prova 5km.pdf
├── Documentacao_Tecnica_Completa_5KM.docx
├── README.md                # Documentação principal do repositório
├── Relatório Executivo Impresso - Prova 5km.pdf
├── Relatorio_Executivo_5KM.docx
└── requirements.txt         # Lista de dependências Python para reprodutibilidade

---

## 📊 Pipeline de Processamento de Dados

O tratamento dos dados é 100% programático, respeitando o princípio da **imutabilidade da camada Raw**:

1. **Ingestão e Codificação:** Leitura de dados brutos tratando encodings específicos (`utf-8-sig`) para eliminação do caractere de ordem de bytes (BOM).
2. **Normalização Temporal:** Conversão automatizada de strings no formato `HH:MM:SS` para minutos decimais (`float64`) utilizando parsing de `pd.to_timedelta`, eliminando falhas de tipo numérico decorrentes da formatação brasileira de numerais.
3. **Tratamento de Inconsistências:** Remoção defensiva de registros com falhas de cronometragem ou incompletos ($N_{bruto} = 1563 \rightarrow N_{válido} = 1219$).

---

## 📈 Principais Resultados Encontrados

### 1. Panorama Geral ($N = 1219$)
* **Tempo Médio:** $39,60$ minutos
* **Tempo Mediano:** $38,05$ minutos
* **Desvio Padrão:** $10,18$ minutos
* **Intervalo de Maior Frequência:** $37,53$ a $43,85$ minutos (com 284 atletas, representando $23,30\%$ da prova).
* **Número de Classes (Sturges):** $k = 11$ classes.

### 2. Segmentação por Gênero
| Indicador | Feminino (F) | Masculino (M) |
| :--- | :---: | :---: |
| **Amostra ($N$)** | 590 atletas ($48,4\%$) | 629 atletas ($51,6\%$) |
| **Média** | $43,11$ min | $35,85$ min |
| **Mediana** | $42,02$ min | $34,00$ min |
| **Desvio Padrão** | $9,33$ min | $9,83$ min |
| **Mínimo / Máximo** | $22,88$ min / $74,95$ min | $18,57$ min / $88,08$ min |

---

## 🚀 Como Executar o Projeto

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/5km-pesquisa-descritiva.git
   cd 5km-pesquisa-descritiva
   ```

2. **Criar e Ativar o Ambiente Virtual:**
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   ```

3. **Instalar as Dependências:**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

4. **Executar o Pipeline de Scripts:**
   ```bash
   python src/04_tabela_frequencias.py
   python src/05_gerar_graficos.py
   python src/06_segmentacao_genero.py
   python src/07_graficos_genero.py
   ```

Os relatórios intermediários em `.csv` e as imagens em alta resolução (`.png`) serão atualizados na pasta `dados/processed/`.

---

## ✒️ Licença e Metodologia

Este estudo foi desenvolvido para fins acadêmicos e de portfólio técnico, seguindo as diretrizes metodológicas de Estatística Descritiva aplicadas à administração pública e gestão de eventos.
# 📊 Análise Financeira com Python para o Imposto de Renda  

## 📌 Sobre o Projeto  
Este projeto tem como objetivo **automatizar a análise de extratos bancários** para facilitar o controle financeiro e a declaração do **Imposto de Renda**.  
Com **Python e Pandas**, conseguimos processar os dados do extrato, identificar as **entradas mensais** e calcular o **total recebido no ano**.  

## 🚀 Funcionalidades  
✅ **Carregamento do extrato bancário** (Excel)  
✅ **Limpeza e tratamento dos dados**  
✅ **Conversão de datas e valores monetários**  
✅ **Agrupamento dos ganhos por mês**  
✅ **Cálculo do total do ano**  

## 🛠️ Tecnologias Utilizadas  
- **Python** 🐍  
- **Pandas** 🏛️  
- **OpenPyXL** 📂  

## 📂 Estrutura do Projeto  

pip install pandas openpyxl
python script.py


## 🖥️ Código  
```python
import pandas as pd

# Carregar o extrato bancário
df = pd.read_excel("extrato.xlsx", engine="openpyxl")

# Remover colunas desnecessárias
df.drop(columns=["Status"], inplace=True)

# Converter a coluna "Data" para datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d-%m-%Y", errors="coerce")

# Limpar e converter a coluna "Valor"
df["Valor"] = (
    df["Valor"]
    .astype(str)
    .str.replace(r"[R$\s]", "", regex=True)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Criar a coluna "Mes_Ano" para análise mensal
df["Mes_Ano"] = df["Data"].dt.to_period("M")

# Filtrar apenas as entradas financeiras
df_entradas = df[df["Tipo"] == "entrada"]

# Agrupar os valores por mês
entradas_por_mes = df_entradas.groupby("Mes_Ano")["Valor"].sum().reset_index()

# Calcular o total do ano
total_ano = entradas_por_mes["Valor"].sum()

# Exibir os resultados
print(entradas_por_mes)
print(f"\nValor total do ano: R$ {total_ano:,.2f}")


📌 Autor: Belchior Sobanski
🔗 GitHub: github.com/Belsobanski
📢 LinkedIn: linkedin.com/in/belchior-sobanski

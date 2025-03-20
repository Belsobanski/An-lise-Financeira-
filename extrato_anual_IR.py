import pandas as pd

# Definir caminhos dos arquivos
arquivo_original = "C:/Users/Belchior/Desktop/IR/extrato.xlsx"
arquivo_modificado = "C:/Users/Belchior/Desktop/IR/extrato_modificado.xlsx"
arquivo_final = "C:/Users/Belchior/Desktop/IR/extrato_modificado_2.xlsx"

# 1. Carregar o arquivo original
df = pd.read_excel(arquivo_original, engine="openpyxl")
print("Arquivo Original:")
print(df.head())

# 2. Remover a coluna "Status, espaços,pontos, virgular, R$ do valor e ajuste datatime"
df.drop(columns=["Status"], inplace=True)

# 3. Salvar mudanças no arquivo modificado
df.to_excel(arquivo_modificado, index=False, engine="openpyxl")

# 4. Reabrir o novo arquivo
df = pd.read_excel(arquivo_modificado, engine="openpyxl")
print("\nApós Remover 'Status':")
print(df.head())

# 5. Converter a coluna "Data" para o formato datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d-%m-%Y", errors="coerce")

# 6. Limpar e converter a coluna "Valor" para número
df["Valor"] = (
    df["Valor"]
    .astype(str)  # Garante que os valores são strings antes da substituição
    .str.replace(r"[R$\s]", "", regex=True)  # Remove "R$", espaços e caracteres invisíveis
    .str.replace(".", "", regex=False)  # Remove pontos dos milhares
    .str.replace(",", ".", regex=False)  # Troca a vírgula decimal por ponto
    .astype(float)  # Converte para número
)

# 7. Salvar mudanças no segundo arquivo modificado
df.to_excel(arquivo_final, index=False, engine="openpyxl")

# 8. Reabrir o arquivo final
df = pd.read_excel(arquivo_final, engine="openpyxl")
print("\nArquivo Final Processado:")
print(df.head())

# 9. Criar uma nova coluna "Mes_Ano"
df["Mes_Ano"] = df["Data"].dt.to_period("M")

# 10. Filtrar apenas as entradas
df_entradas = df[df["Tipo"] == "entrada"]

# 11. Agrupar entradas por mês e calcular o total
entradas_por_mes = df_entradas.groupby("Mes_Ano")["Valor"].sum().reset_index()
print("\nEntradas por Mês:")
print(entradas_por_mes)

# 12. Calcular o total do ano
total_ano = entradas_por_mes["Valor"].sum()
print(f"\nValor total do ano: R$ {total_ano:,.2f}")

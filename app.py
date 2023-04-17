import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# título da aplicação
st.title("Retorno Anual X CDI Anual")

# carrega o arquivo de dados
df = pd.read_excel("Verde-GER-rentabilidades.xlsx")

# seleciona as colunas relevantes
df_rentabilidade = df[["Unnamed: 0","Acumulado Ano", "CDI", "Acumulado fundo", "Acum. CDI*"]].copy()

# converte as colunas para float
df_rentabilidade.loc[:, "CDI"] = df_rentabilidade["CDI"].astype(float)
df_rentabilidade.loc[:, "Acumulado Ano"] = df_rentabilidade["Acumulado Ano"].astype(float)

# cria o gráfico
fig, ax = plt.subplots(figsize=(10, 10))
df_rentabilidade.plot.bar(x="Unnamed: 0", y=["Acumulado Ano", "CDI"], ax=ax)
ax.set_xlabel("Ano")
ax.set_ylabel("Retorno (%)")
ax.legend(["Retorno Anual", "CDI Anual"])

# exibe o gráfico na aplicação
st.pyplot(fig)

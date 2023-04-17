import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Verde-GER-rentabilidades.xlsx")
df_rentabilidade = df[["Unnamed: 0","Acumulado Ano", "CDI", "Acumulado fundo", "Acum. CDI*"]]
df_rentabilidade["CDI"] = df_rentabilidade["CDI"].astype(float)
df_rentabilidade["Acumulado Ano"] = df_rentabilidade["Acumulado Ano"].astype(float)
df_rentabilidade.plot.bar(x="Unnamed: 0", y=["Acumulado Ano", "CDI"], figsize = (10,10))
plt.title("Retorno Anual X CDI Anual")
plt.xlabel("Ano")
plt.ylabel("Retorno (%)")
plt.show()
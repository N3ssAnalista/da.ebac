# código de geração do gráfico

import seaborn as sns
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço médio da venda de gasolina em São Paulo')


  # código para salvar figura png

import pandas as pd
import matplotlib.pyplot as plt
grafico.set_title("gasolina", fontsize=12, fontweight="bold")

grafico.set_xlabel("dia", fontsize=10)

grafico.set_ylabel("venda", fontsize=10)

fig = grafico.get_figure()

fig.savefig("gasolina.png")

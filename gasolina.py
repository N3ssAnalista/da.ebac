import pandas as pd
import matplotlib.pyplot as plt

grafico.set_title("gasolina", fontsize=12, fontweight="bold")

grafico.set_xlabel("dia", fontsize=10)

grafico.set_ylabel("venda", fontsize=10)

fig = grafico.get_figure()

fig.savefig("gasolina.png")
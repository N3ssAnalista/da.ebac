# código do gráfico


import matplotlib.pyplot as plt



plt.plot(x, y, marker='o', linestyle='-', color='c')
plt.xlabel('Dia')
plt.ylabel('Venda')
plt.title('Preço médio da Gasolina ')
plt.legend('Valor')
plt.grid(True)
plt.savefig("gasolina.png")
plt.show()
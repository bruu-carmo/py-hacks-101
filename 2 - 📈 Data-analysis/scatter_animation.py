# Gráfico de dispersão com animação simples

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

plt.scatter(x, y, c=colors, alpha=0.5)
plt.title("Scatter Animation Simulado")
plt.show()

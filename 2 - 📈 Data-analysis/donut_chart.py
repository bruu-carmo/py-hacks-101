# Geração de gráfico donut com matplotlib

import matplotlib.pyplot as plt

sizes = [25, 35, 40]
labels = ['A', 'B', 'C']
plt.pie(sizes, labels=labels, wedgeprops=dict(width=0.4))
plt.title("Donut Chart")
plt.show()

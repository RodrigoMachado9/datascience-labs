import matplotlib.pyplot as plt
import numpy as np

grupos = 5
anterior = (30,20,18,17,15)
atual = (40,20,20,10,10)

index = np.arange(grupos)
bar_width = 0.3

barras1 = plt.bar(index, anterior, bar_width, color = 'r', label = '09-03-2020')
barras2 = plt.bar(index + bar_width, atual, bar_width, color = 'b', label='10-03-2020')

plt.xticks(index + bar_width, ('Alana', 'Rodrigo', 'Vitoria', 'Outros', 'Indecisos'))
plt.legend()
plt.show()
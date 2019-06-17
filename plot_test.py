import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [100, 200, 300, 400, 500]

plt.plot(x,y, color='blue', label='Temperatura')
plt.title('Temperatura Ambiente')
plt.xlabel("Tiempo (s)")
plt.ylabel("Grados Celcius")
plt.legend(facecolor='lightgray', shadow=True)
plt.show()
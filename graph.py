import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('25092026/iris_data.csv')

d1 = df[df["Species"] == "Iris-setosa"]
d2 = df[df["Species"] == "Iris-versicolor"]
d3 = df[df["Species"] == "Iris-virginica"]

# Теперь графики для каждого по отдельности. Нужно построить SepalLenghtCm от SepalWidth, SepalLenghtCm от PetalLenghtCm, SepalLenghtCm от PetalWidthCm, SepalWidthCm от PetalLenghtCm, SepalWidthCm от PetalWidthCm, PetalLenghtCm от PetalWidthCm 

plt.scatter(d1["SepalWidthCm"], d1["SepalLengthCm"],color = "red")
plt.scatter(d2["SepalWidthCm"], d2["SepalLengthCm"],color = "blue")
plt.scatter(d3["SepalWidthCm"], d3["SepalLengthCm"],color = "green")
#Для красных видна зависимость линейная, сделаю МНК
k1, b1 = np.polyfit(d1["SepalWidthCm"], d1["SepalLengthCm"], 1)
plt.plot(d1["SepalWidthCm"], k1*d1["SepalWidthCm"]+b1, color= "red", linewidth = 2 )
plt.grid(True)
plt.legend()
plt.show()

plt.scatter(d1["PetalLengthCm"], d1["SepalLengthCm"],color = "red")
plt.scatter(d2["PetalLengthCm"], d2["SepalLengthCm"],color = "blue")
plt.scatter(d3["PetalLengthCm"], d3["SepalLengthCm"],color = "green")
plt.ylabel("SepalLength")
plt.xlabel("PetalLength")
k2, b2 = np.polyfit(d2["PetalLengthCm"], d2["SepalLengthCm"], 1)
k3, b3 = np.polyfit(d3["PetalLengthCm"], d3["SepalLengthCm"], 1)
#plt.plot(d2["PetalLengthCm"], d2["PetalLengthCm"]*k2+b2, color = "black")
#plt.plot(d3["PetalLengthCm"], d3["PetalLengthCm"]*k3+b3, color = "black")
plt.axline((0, b1), slope=k1, color="black") # функция делает прямую для всей области определения, причем мы получили коэффы при помощи данных, поэтому все гуд
plt.axline((0, b2), slope=k2, color="black")
plt.grid(True)
plt.legend()
plt.show()
# может тут и есть смысл, но я его не вижу
plt.scatter(d1["PetalWidthCm"], d1["SepalLengthCm"],color = "red")
plt.scatter(d2["PetalWidthCm"], d2["SepalLengthCm"],color = "blue")
plt.scatter(d3["PetalWidthCm"], d3["SepalLengthCm"],color = "green")
plt.legend()
plt.grid(True)
plt.xlabel("PetalWidth")
plt.ylabel("SepalLength")
plt.show()

# для красненьких чот есть upd. нету(((())))
plt.scatter(d1["PetalLengthCm"], d1["SepalWidthCm"],color = "red")
plt.scatter(d2["PetalLengthCm"], d2["SepalWidthCm"],color = "blue")
plt.scatter(d3["PetalLengthCm"], d3["SepalWidthCm"],color = "green")
#alp1, bet1= np.polyfit(d1["PetalLengthCm"], d1["SepalWidthCm"],1)
#plt.axline((0,bet1), slope=alp1, color = "black")
plt.legend()
plt.grid(True)
plt.xlabel("PetalLength")
plt.ylabel("SepalWidth")
plt.show()

plt.scatter(d1["PetalWidthCm"], d1["SepalWidthCm"],color = "red")
plt.scatter(d2["PetalWidthCm"], d2["SepalWidthCm"],color = "blue")
plt.scatter(d3["PetalWidthCm"], d3["SepalWidthCm"],color = "green")
plt.grid(True)
plt.legend()
plt.xlabel("PetalWidth")
plt.ylabel("SepalWidth")
plt.show()


plt.scatter(d1["PetalWidthCm"], d1["PetalLengthCm"],color = "red")
plt.scatter(d2["PetalWidthCm"], d2["PetalLengthCm"],color = "blue")
plt.scatter(d3["PetalWidthCm"], d3["PetalLengthCm"],color = "green")
plt.grid(True)
plt.legend()
plt.xlabel("PetalWidth")
plt.ylabel("PetalLength")
# здесь все значения в зоне одной прямой.
alp, b = np.polyfit(df["PetalWidthCm"], df["PetalLengthCm"], 1)
plt.axline((0,b), slope = alp, color = "black")
plt.show()










'''
# для iris-setosa
# для этого растения видна примерно линейная зависимость между длиной и шириной. Попробую построить мнк
g1 = df[df["Species"] == "Iris-setosa"]
k1, b1 = np.polyfit(g1["SepalLengthCm"], g1["SepalWidthCm"],1)
plt.scatter(g1["SepalLengthCm"], g1["SepalWidthCm"], label="Iris-setosa", color="red")
plt.plot(g1["SepalLengthCm"], k1*g1["SepalLengthCm"] + b1, color="red")
plt.xlabel("Sepal Lenght, cm")
plt.show()

#для iris-versicolor

g2 = df[df["Species"] == "Iris-versicolor"]
k2, b2 = np.polyfit(g2["SepalLengthCm"], g2["SepalWidthCm"],1)
plt.scatter(g2["SepalLengthCm"], g2["SepalWidthCm"], label = "Iris-versicolor", color="green")
plt.xlabel("Sepal Length cm")
plt.ylabel("Sepal Width cm")
plt.plot(g2["SepalLenght"])
'''

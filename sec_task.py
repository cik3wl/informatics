import matplotlib.pyplot as plt
import numpy as np

steps = np.random.choice([-1, 1], 1000)
x = np.cumsum(steps)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x)
plt.title("Траектория 1 частицы")
plt.xlabel("Шаги N")
plt.ylabel("Положение x")

finals = []
for _ in range(1000):
    walk = np.cumsum(np.random.choice([-1, 1], 1000))
    finals.append(walk[-1])

plt.subplot(1, 3, 2)
plt.hist(finals, bins=30, edgecolor="black")
plt.title("Гистограмма 1000 частиц")
plt.xlabel("Конечное x")

all_walks = np.cumsum(np.random.choice([-1, 1], size=(1000, 1000)), axis=1)

std_by_step = np.std(all_walks, axis=0)

plt.subplot(1, 3, 3)
plt.plot(std_by_step, label="Эксперимент")
plt.plot(np.sqrt(np.arange(1, 1001)), "--", label="Теория $\\sqrt{N}$")
plt.title("Зависимость от N")
plt.xlabel("Шаги N")
plt.ylabel("std(x)")
plt.legend()

plt.tight_layout()
plt.show()
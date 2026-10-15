import matplotlib.pyplot as plt
import math

x = [-5 + i * (10 / 499) for i in range(500)]
y = [2 * xi + (math.sin(xi)) ** 2 + 3 for xi in x]

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.grid(True)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("po.pdf", bbox_inches="tight")
plt.show()
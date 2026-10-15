import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("scores.csv", skipinitialspace=True)
df.columns = df.columns.str.strip().str.lower()
df["student"] = df.index

ax = df.plot.scatter(x="student", y="math", color="red", label="math")
df.plot.scatter(x="student", y="python", color="blue", label="python", ax=ax)
df.plot.scatter(x="student", y="database", color="yellow", label="database", ax=ax)
plt.savefig("scattered.png")
plt.close()

df[["math", "python", "database"]].plot.hist(subplots=True, layout=(1, 3), figsize=(9, 3))
plt.tight_layout()
plt.savefig("histo.png")
plt.close()

df[["math", "python", "database"]].plot.box()
plt.savefig("box.png")
plt.close()
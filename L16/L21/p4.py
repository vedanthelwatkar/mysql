import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("kr.csv")

subjects= data["subjects"]
kishan= data["kishan"]
roshan = data["roshan"]

plt.plot(subjects,kishan,label="Kishan",linewidth=4,color="red",marker="o",
markerfacecolor="yellow",markersize=7)
plt.plot(subjects,roshan,label="Roshan",linewidth=4,color="blue",marker="s",
markerfacecolor="green",markersize=7)
plt.legend(shadow=True)

plt.show()
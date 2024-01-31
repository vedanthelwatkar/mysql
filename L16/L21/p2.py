
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("amit.csv")

subjects =data["subjects"]
marks=data["marks"]
plt.plot(subjects,marks,linewidth=4,marker ="s",markersize=10,markerfacecolor="red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's  Score")
plt.grid()
plt.savefig("amit's score.pdf")
plt.savefig("amit's score.png")
plt.show()


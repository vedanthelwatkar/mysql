import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("roshan.csv")
print(data)
subjects = data["subjects"]
roshan = data["roshan"]

plt.bar(subjects,roshan,width=0.30,color="green")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Roshan's Marks")
plt.show()
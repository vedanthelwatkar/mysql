import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("kr.csv")
print(data)
subjects = data["subjects"]
roshan = data["roshan"]
kishan = data["kishan"]
s = np.arange(len(subjects))

plt.xticks(s,subjects)
plt.bar(s-0.2,roshan,width=0.30,color="green",label="Roshan")
plt.bar(s+0.2,kishan,width=0.30,color="red",label="Kishan")
plt.legend(shadow=True)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title( "Student's Marks")
plt.show()
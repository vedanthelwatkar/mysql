import matplotlib.pyplot as plt
subjects = ["phy","chem","maths"]
marks = [88,44,99]

plt.plot(subjects,marks,linewidth=4,marker="o",markersize=10,markerfacecolor="red")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Amit's Score")
plt.grid()
plt.savefig("amit.png")
plt.savefig("amit.pdf")
plt.show()
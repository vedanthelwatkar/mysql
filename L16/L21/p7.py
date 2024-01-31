import matplotlib.pyplot as plt

expenses= ["food","travel","mobile","shopping"]
amount=[250,300,550,1000]
plt.pie(amount,labels=expenses,autopct="%.2f%%",
colors = ["lightblue","peachpuff","azure","honeydew"],
explode=[0.10,0.0,0.0,0.0], shadow=True)
plt.show()

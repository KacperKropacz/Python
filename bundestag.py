import matplotlib.pyplot as plt
import numpy as np

y = np.array([28, 26, 16, 12, 11, 5, 2])
mylabels = ["SPD", "CDU/CSU", "Greens", "FDP", "AFD", "Left Party", "Others"]
myexplode = [0, 0, 0, 0, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, autopct = '%.0f%%')
plt.show() 
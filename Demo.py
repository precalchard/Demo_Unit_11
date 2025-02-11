print("I did task 2.")

import numpy as np
import matplotlib.pyplot as plot

x= np.array(["Croissant", "Danish", "Bear Claw", "Coffee Cake", "Cinnamon Roll"])
y= np.array([4, 72, 23, 16, 91])
plot.bar(x,y)

plot.xlabel("Pastries")
plot.ylabel("Amount")
plot.title("Pastries in a café")

plot.savefig("pastries_bar_graph.png")
plot.show()
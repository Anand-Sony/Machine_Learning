import matplotlib.pyplot as plt
import numpy as np

categories = ["Categories A" ,"Categories B" , "Categories C" , "Categories D"]
data = [1,2,3,4]

plt.bar(categories , data , color=["orange", "Pink"] , edgecolor="black" )
plt.xlabel('Categories')
plt.ylabel('Data')
plt.title('Bar Chart')
plt.show()
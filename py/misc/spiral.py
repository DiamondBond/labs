
import numpy as np 
import matplotlib.pyplot as plt 
  
  
# setting the axes 
# projection as polar 
plt.axes(projection = 'polar') 
  
# creating an array 
# containing the radian values 
rads = np.arange(0, 2 * np.pi, 0.001)  
  
# plotting the spiral 
for rad in rads: 
    r = rad 
    plt.polar(rad, r, 'g.') 
      
# display the polar plot 
plt.show()

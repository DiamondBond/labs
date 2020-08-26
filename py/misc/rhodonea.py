
import numpy as np 
import matplotlib.pyplot as plt 
  
  
# setting the axes 
# projection as polar 
plt.axes(projection='polar') 
  
# setting the length 
# and number of petals 
a = 1
n = 6
  
# creating an array 
# containing the radian values 
rads = np.arange(0, 2 * np.pi, 0.001)  
  
# plotting the rose 
for rad in rads: 
    r = a * np.cos(n*rad) 
    plt.polar(rad, r, 'g.') 
   
# display the polar plot 
plt.show() 

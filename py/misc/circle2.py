
import numpy as np 
import matplotlib.pyplot as plt 
import math 
  
  
# setting the axes 
# projection as polar 
plt.axes(projection = 'polar') 
  
# setting the values of 
# semi-major and 
# semi-minor axes 
a = 4
b = 3
  
# creating an array 
# containing the radian values 
rads = np.arange(0, (2 * np.pi), 0.01) 
  
# plotting the ellipse 
for rad in rads: 
    r = (a*b)/math.sqrt((a*np.sin(rad))**2 + (b*np.cos(rad))**2) 
    plt.polar(rad, r, 'g.') 
  
# display the polar plot 
plt.show() 

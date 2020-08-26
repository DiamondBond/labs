
# importing the modules  
from bokeh.plotting import figure, output_file, show  
  
# file to save the model  
output_file("gfg.html")  
       
# instantiating the figure object  
graph = figure(title = "Bokeh Quadratic Graph")  
  
# name of the x-axis  
graph.xaxis.axis_label = "x-axis"
       
# name of the y-axis  
graph.yaxis.axis_label = "y-axis"
  
# points to be plotted 
x0 = [1, 0, 0] 
y0 = [4, 8, 5] 
x1 = [5, 4, 4] 
y1 = [4, 8, 7] 
cx = [2.5, 2, 4] 
cy = [8, 3, 4] 
  
# line color value of the quadratic 
line_color = ["yellow", "red", "purple"] 
  
# line width value of the quadratic 
line_width = [10, 5, 8] 
  
# plotting the graph  
graph.quadratic(x0, y0, 
                x1, y1, 
                cx, cy, 
                line_color = line_color, 
                line_width = line_width)  
       
# displaying the model  
show(graph) 

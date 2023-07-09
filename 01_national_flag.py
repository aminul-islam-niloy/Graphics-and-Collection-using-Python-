import matplotlib.pyplot as plot
import matplotlib.patches as patch

fig, axis = plot.subplots(figsize=(10,6))
# create a figure and one or more subplots (axes) within that figure

rect = patch.Rectangle((0,0),10,6, facecolor = 'forestgreen')
axis.add_patch(rect)
# single subplot or axis within a figure

circle = patch.Circle((4.5, 3), radius=2, facecolor = 'red')

axis.add_patch(circle)
axis.set_xlim(0,10)
axis.set_ylim(0,6)
plot.title('National Flag')
# plot.axis('off') 
plot.show()



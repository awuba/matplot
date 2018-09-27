import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # create a RandomWalk instane and draw all points
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # set figure size
    plt.figure(figsize=(9, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, 
            edgecolor='none', s=1)
    
    # redraw begin point and end point
    plt.scatter(0, 0, c='green', edgecolor='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolor='none', s=20)
    
    # hide label
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

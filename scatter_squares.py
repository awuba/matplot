import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolor='none', s=40)

# set title and add label
plt.title("Squre Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# set scale size
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')

import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.scatter(x_value, y_value, s=200)

# set title and add label
plt.title("Squre Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# set scale size
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

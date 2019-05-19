import matplotlib.pyplot as plt

# Plot the first 5 numbers
# input_values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]

# Plot the first 5000 numbers
input_values = list(range(1, 5001))
cubes = [x * x * x for x in input_values]

plt.plot(input_values, cubes, linewidth=5)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
plt.axis([0, 5000, 0, 125000000000])

plt.show()

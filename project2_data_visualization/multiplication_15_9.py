from die import Die
import pygal

# Create two D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = [ die_1.roll() * die_2.roll() for roll_num in range(1000) ]

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [ results.count(value) for value in range(1, max_result + 1) ]

# Visualize the results.
hist = pygal.Bar()

hist.x_labels = [ (str(i)) for i in range(1, max_result + 1) ]
hist.title = "Results of rolling two D6 1000 times."
hist.x_title = "Result"
hist.y_title = "Frequency of Multiplication"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_multplication_visual.svg')

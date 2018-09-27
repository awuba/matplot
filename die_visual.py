import pygal
from die import Die

# create a D6
die = Die()

# roll die
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analize result
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visual results
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.xlabels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

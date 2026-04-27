#Question 2:
#Create different histogram charts for rolling two six-sided die, or two eight-sided die. Use the example from the textbook resources, “dice_visual.py.” Discuss the     differences and similarities of the distribution of the results. In general, how does this correlate with the distribution of two n-sided die. Search for relevant discussions on the internet.
#8 sided

import plotly.express as px
from die import Die

#create two D8 dice
die_1 = Die(8)
die_2 = Die(8)

#roll dice
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

frequencies = []
for value in poss_results:
    frequencies.append(results.count(value))

#plot
title = "Results of rolling two D8 Dice "
labels = {'x' : 'Result' , 'y' : 'Frequency' }

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

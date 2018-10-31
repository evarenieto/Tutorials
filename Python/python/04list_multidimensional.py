#Multidimensional list
#A list inside in a list

#Time, travel, expenses...

travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]
print("Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number, sum(week)))
    week_number += 1
#you shoul obtein something like this:
#Travel Expenses:
#* Week #1: $29.75
#* Week #2: $75.25
#* Week #3: $42.25

#Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.

#Then, print the result of calling the my_dict.items().

my_dict= {
  'Boyfriend':'Dan',
  'Age': '41',
  'Race': 'other european'
}
print(my_dict.items())


#Remove your call to .items() and replace it with a call to .keys() and a call to .values(), each on its own line.
#Make sure to print both!
my_dict= {
  'Boyfriend':'Dan',
  'Age': '41',
  'Race': 'other european'
}
print(my_dict.keys())
print(my_dict.values())
print(my_dict)

#For each key in my_dict: print out the key ,
#then a space, then the value stored by that key. (You should use print a, b rather than print a + " " + b.)
my_dict= {
  'Boyfriend':'Dan',
  'Age': '41',
  'Race': 'other european'
}

for key in my_dict:
  print(key, my_dict[key])

#Check out the list comprehension example in the editor. When you're pretty sure you know what it'll do,
#click Run to see it in action.

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

#Use a list comprehension to build a list called even_squares in the editor.
#Your even_squares list should include the squares of the
#even numbers between 1 to 11. Your list should start [4, 16, 36...] and go from there.

even_squares = [x ** 2 for x in range(1,11) if x % 2 == 0]

print(even_squares)

#Use a list comprehension to create a list, cubes_by_four.
#The comprehension should consist of the cubes of the
#numbers 1 through 10 only if the cube is evenly divisible by four.
#Finally, print that list to the console.
#Note that in this case, the cubed number should be
#evenly divisible by 4, not the original number.

cubes_by_four = [ x ** 3 for x in range(1,11) if x % 2 == 0]
print(cubes_by_four)



#Use list slicing to print out every odd element of my_list from start to finish.
#Omit the start and end index. You only need to specify a stride.
#Check the Hint if you need help.

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

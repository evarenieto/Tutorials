#Alright, my list is messy! Help me clean it up!
#First, start by moving the 1 from index 3 to index 0. Try to do this in a single step by using both .pop() and .insert(). It's OK if it takes you more than one step, though!



messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

messy_list.insert(0, messy_list.pop(3))

#now, delete the string, the boolean and the list
>>> messy_list
[1, 'a', 2, 3, False, [1, 2, 3]]
>>> messy_list.remove('a')
>>> del messy_list[3]
>>> messy_list.remove([1, 2, 3])
>>> messy_list
[1, 2, 3]
>>>

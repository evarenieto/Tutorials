print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"

#Let's simplify things by making the letters in our word lowercase.
#We also need to grab the first letter of the word.
#Inside your if statement:
#Create a new variable called word that holds the .lower()-case conversion of original.
#Create a new variable called first that holds word[0], the first letter of word.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
else:
    print 'empty'

#Move it on Back
#Now that we have the first letter stored, we need to add both the letter and the
#string stored in pyg to the end of the original string.
#Remember how to concatenate (i.e. add) strings together?

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
    print 'empty'


#Ending Up
#Well done! However, now we have the first letter showing up both at the beginning and near the end.

#s = "Charlie"

#print s[0]
# will print "C"

#print s[1:4]
# will print "har"
#First we create a variable s and give it the string "Charlie"
#Next we access the first letter of "Charlie" using s[0]. Remember letter positions start at 0.
#Then we access a slice of "Charlie" using s[1:4]. This returns everything from the letter at position 1 up till position 4.
#We are going to slice the string just like in the 3rd example above.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'


#Testing, Testing, is This Thing On?
#Yay! You should have a fully functioning Pig Latin translator. Test your code thorougly to be sure everything is working smoothly.

#You'll also want to take out any print statements you were using to help debug intermediate steps of your code. Now might be a good
#time to add some comments too! Making sure your code is clean, commented, and fully functional is just as important as writing it in
#the first place.

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'    

#let do another examples to play with lists
quote = "To go to the toilet i need"
words = quote.split()
words
#can you see waht split does?
#===>['To', 'go', 'to', 'the', 'toilet', 'i', 'need']

import time
for word in words:
    #sleep function(.5) will give us a word every 5 sec
    print(word)
    time.sleep(.5)
#its will return
#...
#To
#go
#to
#the
#toilet
#i
#need
dogs = ["Willy", "Luci"]
ocassional_dogs = ["Teddy", "Braco"]
to_line = ", ".join(dogs)
cc_line = ", ".join(ocassional_dogs)
print("To:   " + to_line)
print("Cc:   " + cc_line)

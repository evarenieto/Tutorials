name = input("what´s your name?")
question = input("{}, do you understand while loops?".format(name))
while question != "yes":
    print("Ok, {}, let´s make some research:www.python.org".format(name))
    question = input("{}, now do you undestand?".format(name))
print("Great!".format(name))

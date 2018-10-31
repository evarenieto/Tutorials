first_name = input("what is your first name?   ")
print("Hello,", first_name)
if first_name == "Luci":
    print(first_name, "is learning AI")
elif first_name == "Eva":
    print(first_name,"is learning Python on Tree House for 40 pound/month")
else:
    age = int(input("How old are you?"))
    if age <= 6:
        print("Wow you are {}! If you feel confident ...".format(age))
    print("You should learn some AI, {}!".format(first_name))
print("Have a great day, {}!".format(first_name))
#favorite_color = input("What is your favorite color? ")
#favorite_color
#with round function we get the close number: 8.9 = 9
#round(8.9)
#Auto fill email, for example
#"Thank for learning Ruby with my Dani"
#Subject_template = "Thank for learning {} with my, {}"
#Subject_template.format("Python", "Eva")
#Subject_template
#different application of .format
#"you just bought {} {}.".format("5", "potatoes")

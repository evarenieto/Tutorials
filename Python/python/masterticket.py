service_charge = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
  return (number_of_tickets * TICKET_PRICE) + service_charge


while tickets_remaining >= 1:
  print("There are {} tickets remaining.".format(tickets_remaining))
  name = input("What is your name?")
  number_tickets = input("Hello {}, how many ticket would you like?".format(name))
  try:
    number_tickets = int(number_tickets)
    if number_tickets > tickets_remaining:
      raise ValueError("There are only {} ticket remaining."  .format(tickets_remaining))
  except ValueError as err:
    print("Sorry, there is a issue: {} Please try again"   .format(err))
  else:
    name_cost = calculate_price(number_tickets)
    print("The total due is ${}".format(name_cost))
    question = input("Do you want to proceed?    Y/N?   ")
    if question.lower() != "n":
        print("SOLD!")
      #count = tickets_remaining -= int(number_tickets)
        tickets_remaining -= int(number_tickets)
        print("Thank you {}"  .format(name))
      #print("We have {} tickets remaining."     .format(count))
    else:
        print("Thank you anyways, {}!"  .format(name))


print("Sorry, no more tickets available")

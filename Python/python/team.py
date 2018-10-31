players = []

add_players = input("Woul you like to add a player name to the list?  (Yes/No)  ")
# If the user answers "Yes", let them type in a name and add it to the list.
while add_players.lower() == "yes":
  name = input("Enter the name of a player to add the team:")
  players.append(name)
  add_players = input("Would you like to add another player?  (Yes/No)  ")
print("There are {} players on the team."  .format(len(players)))

player_number = 1
for player in players:
  print("Player {}: {}"   .format(player_number, player))
  player_number += 1

goal_keeper = input("Selec the goal keeper by selecting the player number.  (1-{})".format(len(players)))
goal_keeper = int(goal_keeper)
# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great!! The goalkeepet for the game will be {}".format(players[goal_keeper - 1]))

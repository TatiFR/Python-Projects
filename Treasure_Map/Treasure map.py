print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# First crossroad - left or right (left = game over)
route = input('You arrive at a fork in the road and need to decide if you should turn left or right. Type "left" or "right" ')
if route  == "right" or route == "Right":
  print("The path you have chosen is easy to walk along, however you come across a lake.")
  transport = input('Do you swim across the lake or wait for the ferry? Type "swim" or "ferry". ')
  if transport == "ferry" or transport == "Ferry":
    print("You safely cross the lake arriving to an island.")
    door = input('On the island you come across three buildings. One with a blue door, one with a yellow door and another with a red door. Which door do you open? Type "blue", "yellow" or "red". ')
    if door == "blue" or door == "Blue":
      print("You've arrived! You opened the door to the treasure")
    else: 
      print("This door was a trap, a pack of werewolves were waiting for you. Game over!")
  else:
    print("The water was infested with crocodiles. Game over!")
else:
  print("You come across a swarm of bees and get sting. You're allergic... Game over!")

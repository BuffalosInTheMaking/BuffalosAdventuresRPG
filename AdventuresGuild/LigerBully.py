def start():
  print("\nYou find yourself panting from a Liger that chased you across open plains.")
  print("There is a cave you can hid in to your left and river to cross on your right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    cave_entrance()
  elif "r" in answer:
    river_entrance()
  else:
    game_over("Your poor decision making led the Liger right to you!")


# start the game
start()
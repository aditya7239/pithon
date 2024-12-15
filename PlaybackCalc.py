def playback_time(play_time, playback_speed):
  play_time = play_time * 60
  playback_time = play_time / playback_speed
  minutes = int(playback_time // 60)
  seconds = int(playback_time % 60)
  return f"{minutes:02d}:{seconds:02d}"

playback_speeds = [0.25, 0.5, 0.75, 1.25, 1.5, 1.75, 2]

while True:
  user_input = input("Enter the play time in minutes or exit to quit: ")
  if user_input.lower() == "exit":
    break
  try:
    play_time = float(user_input)
    if play_time > 0:
      print(f"Play time: {play_time} minutes")
      print("Playback speed | Playback time")
      print("----------------|--------------")
      for playback_speed in playback_speeds:
        result = playback_time(play_time, playback_speed) # Changed the variable name here
        print(f"{playback_speed:12.2f} | {result:12s}") # Changed the variable name here
      print()
    else:
      print("Invalid input: play time must be positive.")
  except ValueError:
    print("Invalid input: play time must be a number.")

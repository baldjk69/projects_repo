# Note-Taking App
def noteTakingApp():
  print("Note-Taking App")
  print("1. Add notes")
  print("2. View notes")
  print("3. Quit")
  option = int(input("Select an option : "))

  if(option == 1):
    note = input("New note : ")
    with(open("notes.txt", "a") as f):
      f.write(note + '\n')
    noteTakingApp()

  elif(option == 2):
    with(open("notes.txt", "r") as f):
      notes = f.read()
      print(notes)
    noteTakingApp()

  elif(option == 3):
    exit()

  else:
    print("Invalid option")

noteTakingApp()
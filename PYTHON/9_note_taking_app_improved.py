# Note-Taking App
def noteTakingApp():
  while True:
    print("Note-Taking App")
    print("1. Add notes")
    print("2. View notes")
    print("3. Quit")

    option = (input("Select an option : "))
    file_path = "(9-12) Python Applied & Git/9_notes.txt"

    if option == "1":
      note = input("New note : ")
      with open(file_path, "a") as f:
        f.write(note + '\n')
      print("Note added successfully!")

    elif option == "2":
      try:
        with(open(file_path, "r") as f):
          notes = f.read()
          if notes.strip() == "":
            print("No notes yet.")
          else:
            print("\nYour notes:")
            print("--------------------")
            print(notes)
            print("--------------------")
      except FileNotFoundError:
        print("No notes found. Try adding one first.")

    elif(option == "3"):
      print("Goodbye!")
      break

    else:
      print("Invalid option")

# Run the app
noteTakingApp()
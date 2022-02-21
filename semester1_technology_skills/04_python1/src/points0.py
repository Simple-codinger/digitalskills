from cs50 import get_int

def main():
  # Prompt user for points
  points = get_int("Wie viele Punkte hast Du verloren? ")

  MY_POINTS = 2

  # Compare points against mine
  if points < MY_POINTS:
      print("Du hast weniger Punkte verloren als ich.")
  elif points > MY_POINTS:
      print("Du hast mehr Punkte verloren als ich")
  else:
      print("Du hast gleiche viele Punkte wie ich verloren.")

if __name__ == "__main__":
    main()

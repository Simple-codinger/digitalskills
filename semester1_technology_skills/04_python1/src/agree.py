from cs50 import get_string

def main():
  # Prompt user for agree
  answer = get_string("Bist Du einverstanden? ")

  if answer == "j" or answer == "J":
    print("Du bist einverstanden.")
  elif answer == "n" or answer == "N":
    print("Du bist nicht einverstanden.") 

if __name__ == "__main__":
    main()

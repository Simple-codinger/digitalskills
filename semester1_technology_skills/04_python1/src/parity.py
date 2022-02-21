from cs50 import get_int

def main():
  # Prompt user for integer
  n = get_int("n: ")

  # Check parity of integer
  if n % 2 == 0:
      print("gerade")
  else:
      print("ungerade")

if __name__ == "__main__":
    main()

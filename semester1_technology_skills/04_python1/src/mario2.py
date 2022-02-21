from cs50 import get_int

def main():
  while True:
    n = get_int("Height: ")
    if n > 0:
        break

  for i in range(n):
      print("#")

    
if __name__ == "__main__":
    main()
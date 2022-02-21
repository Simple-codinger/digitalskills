from cs50 import get_int

def main():
  while True:
    n = get_int("Size: ")
    if n > 0:
        break

  for i in range(n):
    for j in range(n):
        print("?", end="")
    print()
    
if __name__ == "__main__":
    main()
from cs50 import get_int

def main():
  x = get_int("x: ")
  y = get_int("y: ")
  
  if x < y:
    print("x ist kleiner als y")

  if x < y:
    print("x ist kleiner als y")
  else:
    print("x ist nicht kleiner als y")

  if x < y:
    print("x ist kleiner als y")
  elif x > y:
    print("x ist größer als y")
  elif x == y:
    print("x ist gleich y")
  
  if x < y:
    print("x ist kleiner als y")
  elif x > y:
    print("x ist größer als y")
  else:
    print("x ist gleich y")

if __name__ == "__main__":
    main()
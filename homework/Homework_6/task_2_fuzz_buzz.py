"""FuzzBuzz."""


for y in range(1, 101):
    if y % 3 == 0 and y % 5 == 0:
        print("FuzzBuzz")
    elif y % 3 == 0:
        print("Fuzz")
    elif y % 5 == 0:
        print("Buzz")
    else:
        print(y)

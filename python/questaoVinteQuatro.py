print("How many cats do you have?")
numCats = input()
try:
    if int(numCats)< 0:
        print("Only positive numbers")
    elif int(numCats)>= 4:
        print("That is a lot of cats.")
    else:
        print("That is not that many cats.")
except RuntimeError:
    print("Only int numbers")
except ValueError:
    print("Only int numbers")

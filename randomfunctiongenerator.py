from numpy.random import randint as rand
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
functions = ["ln", "sin", " * ", " / ", "sqrt", "e^", "^"]
random = rand(0, 2)
if random == 0:
  numerator = "" + functions[rand(0, len(functions))] + "("
  denominator = "" + functions[rand(0, len(functions))] + "("
  if numerator == "^(" or numerator == " * (" or numerator == " / (":
    numerator = "" + str(numbers[rand(0, len(functions))]) + numerator
  if denominator == "^(" or denominator == " * (" or denominator == " / (":
    denominator = "" + str(numbers[rand(0, len(numbers))]) + denominator
  for i in range(0, rand(0, 3)):
    numerator += "" + str(numbers[rand(0, len(numbers))])
  for i in range(0, rand(0, 3)):
    denominator += "" + str(numbers[rand(0, len(numbers))])
  denominator += "x)"
  numerator += "x)"
  if len(numerator) < len(denominator):
    if (len(denominator) - len(numerator)) % 2 == 0:
      for i in range(0, (int)((len(denominator) - len(numerator)) / 2)):
        print(" ", end="")
    else:
      for i in range(0, (int)((len(denominator) - len(numerator)) / 2) + 1):
        print(" ", end="")
  print("(" + numerator + ")")
  for i in range(0, max(len(numerator), len(denominator)) + 2):
    print("-", end="")
  print()
  if len(denominator) < len(numerator):
    if (len(numerator) - len(denominator)) % 2 == 0:
      for i in range(0, (int)((len(numerator) - len(denominator)) / 2)):
        print(" ", end="")
    else:
      for i in range(0, (int)((len(numerator) - len(denominator)) / 2) + 1):
        print(" ", end="")
  print("(" + denominator + ")")
else:
  numerator = "" + functions[rand(0, len(functions))] + "("
  if numerator == "^(" or numerator == " * (" or numerator == " / (":
    numerator = "" + str(numbers[rand(0, len(functions))]) + numerator
  for i in range(0, rand(0, 3)):
    numerator += "" + str(numbers[rand(0, len(numbers))])
  numerator += "x)"
  print(numerator)


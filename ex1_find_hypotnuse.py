import math

def hypotenuse(a, b):
   h = math.sqrt(a ** 2 + b ** 2)
   return h

#MAIN
side_1 = float(input("Enter one side of the triangle"))
side_2 = float(input("Enter another side of the triangle"))

hyp = hypotenuse(side_1, side_2)
print(f'The hypotenuse of your triangle is {hyp:.1f}')

def gcf(x,y):
  print("The factors of" ,x, "and" ,y, "are:")
  for i in range(1,x+1):
    if x % i == 0:
      print(i)
  for i in range(1,y+1):
    if y % i == 0:
      print(i)
number1 = 64
number2 = 24
gcf(number1,number2)

    




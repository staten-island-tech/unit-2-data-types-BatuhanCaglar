x = int(input("Enter a number:"))
y = int(input("Enter a second:"))
list = []

def gcf():
  for i in range (x,0,-1):
    if x%i == 0 and y%i == 0:
      list.append(i)
      print (max(list))
gcf()



    




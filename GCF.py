
numb1 = 54
numb2 = 24
def factors(x,y):
    print("The factors of" ,numb1, "and" ,numb2, "are:")
    for i in range(1,numb1+1) and (1,numb2+1):
        if (numb1 % i == 0) and (numb2 % i == 0):
            print(i)
factors(numb1,numb2)







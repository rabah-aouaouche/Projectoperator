x=int(input("tapez le premier numero "))
y=int(input("tapez le deuxieme numero "))
print("enter the operator : ")
operation=input("\n 1 for + \n 2 for - \n 3 for * \n 4 for / ")
if (operation=="1"):
    print("the result of addition is ",x+y)
elif (operation=="2"):
    print("the result of soustraction is ",x-y)
elif (operation=="3"):
    print("the result of multiplication is ",x*y)
elif (operation == "4"):
    print("the result of division is ",x/y)
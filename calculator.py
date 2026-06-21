import math
while True:
    print("1-Addition")
    print("2-Subtraction") 
    print("3-Multiplication")
    print("4-Division")
    print("5-Power")
    print("6-Exit")
    choice=int(input("Enter Your Choice[1,2,3,4,5,6]"))
    if choice in (1,2,3,4,5,):
        num1=float(input("Enter The Number"))
        num2=float(input("Enter The Number "))
        if choice==1:
            print(num1+num2)
        elif choice==2:
            print(num1-num2) 
        elif choice==3:
            print(num1*num2)
        elif choice==4:
            if num2==0:
                print("Error! Cannot divide by zero.")
            else:    
                print(num1/num2)
        elif choice==5:
            print(pow(num1,num2))    
    elif choice==6:
        print("Thanks for using the  calculator!!")
        break
    else:
        print("Invalid Choice")


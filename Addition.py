while True:
    print("1 Addition")
    print("Enter q or Q to exit")
    
    choice = input("Enter your choice")

    if choice == 'q'or choice =='Q':
        break
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2)) 

    print()      

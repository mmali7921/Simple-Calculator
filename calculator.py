
def add(n1,n2):
     print(n1+n2)

def subtract(n1,n2):
    print(n1-n2)

def multiply(n1,n2):
    print(n1*n2)

def divide(n1,n2):
    print(n1/n2)

while(1):
    print("Enter the choice:\n 1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n 5.Exit\n")
    choice = input()
    print("Enter 2 numbers")
    n1 = input()
    n2 = input()
    n1=int(n1)
    n2=int(n2)
    if choice == "1":
        add(n1,n2)
    elif choice == "2":
        subtract(n1,n2)
    elif choice == "3":
        multiply(n1,n2)
    elif choice == "4":
        divide(n1,n2)
    elif choice == "5":
        exit(0)
    else:
        print("Invalid choice")

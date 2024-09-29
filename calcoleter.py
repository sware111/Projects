def Sums(num1, num2):
    return num1 + num2

def Minus(num1, num2):
    return num1 - num2

def Multiple(num1, num2):
    return num1 * num2

def Power(num1, num2):
    return num1 ** num2

def Division_integer(num1, num2):
    return num1 // num2
    
def Division_float(num1, num2):
    return num1 / num2
    

def Message():
    print("Welcom to Calculator".center(60))

def Input_():
    is_Active = True
    while is_Active:
        print("1- Sums")
        print("2- Miuns")
        print("3- Multiple")
        print("4- Power")
        print("5- Division_integer")
        print("6- Division_float")
        print("0- Exit")

        Number = int(input("Enter Choice Operation : "))

        if Number == 1:
            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))
            
            print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Sums(Number1, Number2)}")

        elif Number == 2:
            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))

            print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Minus(Number1, Number2)}")

        elif Number == 3:
            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))

            print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Multiple(Number1, Number2)}")

        elif Number == 4:
            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))

            print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Power(Number1, Number2)}")

        elif Number == 5:
            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))

            if Number2 == 0:
                print(f"Invalid Number, Can't {Number2} Division, Becuase Zero Division")
            elif Number2 != 0:
                print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Division_integer(Number1, Number2)}")

        elif Number == 6:

            Number1 = int(input("Enter First Number: "))
            Number2 = int(input("Enter Second Number: "))
            if Number2 == 0:
                print(f"Invalid Number, Can't {Number2} Division, Becuase Zero Division")
            elif Number2 != 0:
                print(f"First Number is {Number1} and Second Number is {Number2} --> and Result is {Division_float(Number1, Number2)}")

        if Number == 0:
            is_Active = False

def main():
    Message()
    Input_()



main()
print("Good luck!")
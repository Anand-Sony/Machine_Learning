def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def multiply(x,y):
    return x*y
def divide(x,y):
    if(y==0):
        return "Error! Denominator can't be 0"
    return (x/y)

def calculator():

    while True:
        print("Select Operation : ")
        print("1 : Add")
        print("2 : Subtract")
        print("3 : Multiply")
        print("4 : Division")
        choice = input("Enter choices : ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter Second number : "))

            if(choice=='1'):
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif(choice=='2'):
                print(f"{num1} - {num2} = {sub(num1, num2)}")            
            elif(choice=='3'):
                print(f"{num1} * {num2} = {multiply(num1, num2)}")            
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")            

        next = input("Do you want to perform another calculation : ")
        if next.lower() != "yes":
            print("Thanks!")
            break
        
calculator()
def factorial(n):
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)

def fibonacchi(n):
    if n<=1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

def sum_pf_digits(n):
    if n<10:
        return n
    return n%10 + sum_pf_digits( n // 10)

def main():
    while True:
        print("\n Welcome to the section")
        print("\n 1. Factorial of a Number")
        print("\n 2. Fibonacchi of a Number")
        print("\n 3. Sum of the digits of a Number")
        print("\n 4. Exit")
        choice = input("Please enter your choice( 1-4 ) : ")

        if choice == '4':
            print("Bye Bye")
            break

        elif choice == '1':
            try:
                num = int(input("Please enter the number whose factorial you want : "))
                if num<0:
                    print("Please give a valid number, Please provide a positive number..")
                    continue
                result = factorial(num)
                print(f"Factorial of the {num} is : {result}. ")
            except ValueError:
                print("Please give a valid number, Please provide a positive number..")

        elif choice == '2':
            try:
                num = int(input("Please enter the number whose fibonacchi series you want to stop at : "))
                if num<0:
                    print("Please give a valid number, Please provide a positive number..")
                    continue
                result = fibonacchi(num)
                print(f"Fibinacchi of the {num} is : {result}. ")
            except ValueError:
                print("Please give a valid number, Please provide a positive number..")

        elif choice == '3':
            try:
                num = int(input("Please enter the number whose sum series you want : "))
                if num<0:
                    print("Please enter a valid number..")
                    continue
                result = sum_pf_digits(num)
                print(f"The Sum of all the digit of the number {num} is : {result}. ")
            except ValueError:
                print("Please enter a valid number")

        else:
            print("Invalid Choise, Please select 1-4")

if __name__ == "__main__":
    main()          
import math
from datetime import datetime

def calculator():
    version = "1.1"
    print("\n**********************************************************************")
    print("Welcome to Ancod3r's Calculator!\tCalculator Version " + version)
    print("**********************************************************************")

    dtnow = datetime.now()
    logTime = dtnow.strftime("%d/%m/%Y %H:%M:%S")

    file = open('calculator.log', 'a')
    file.write(f"Ancod3r, {logTime}\n\n")

    def press():
        input("\nPress return key to cont...!\n")

    def options():
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplation")
        print("[4] Division")
        print("[5] Factorial")
        print("[6] Square upto Entered Number")
        print("[7] Factorial upto Entered Number")
        print("[8] Table of Entered Number")
        print("[9] Table Upto Entered Number")
        print("[10] Cube upto Entered Number")
        print("[11] Square Root")
        print("[12] Cube Root")
        print("[13] Prime Numbers")
        print("[14] Power")
        print("[15] Calculate Percentage")
        print("[16] Find Sine of a Number")
        print("[17] Find Cosine of a Number")
        print("[18] Find Tangent of a Number")
        print("[19] ABOUT")
        print("[quit] To End The Program")

    options()
    while True:
        user_input = input("\nEnter Option [1-19] => ")

        # Function to check entered number is Float or Integer.
        def cast(num):
            if('.' in num):
                return float(num)
            else:
                return int(num)

        if user_input == '':
            pass

        # Addition
        elif user_input == "1":
            try:
                num1 = cast(input("Enter Number: "))
                num2 = cast(input("Enter Number: "))
                result = str(num1 + num2)
                print("====================================================")
                print(f"  The Addition of '{num1}' And '{num2}' is: '{result}'")
                print("====================================================")
                file.write("\n"+str(num1) + " + " + str(num2) + " = " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred!")
                press()

        # Subtraction
        elif user_input == "2":
            try:
                num1 = cast(input("Enter Number: "))
                num2 = cast(input("Enter Number: "))
                result = str(num1 - num2)
                print("=======================================================")
                print(f"  The Subtraction of '{num1}' And '{num2}' is: '{result}'")
                print("=======================================================")
                file.write("\n"+str(num1) + " - " + str(num2) + " = " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Multiplication
        elif user_input == "3":
            try:
                num1 = cast(input("Enter Number: "))
                num2 = cast(input("Enter Number: "))
                result = str(num1 * num2)
                print("=========================================================")
                print(f"  The Multiplation of '{num1}' And '{num2}' is: '{result}'")
                print("=========================================================")
                file.write("\n"+str(num1) + " x " + str(num2) + " = " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Division
        elif user_input == "4":
            try:
                num1 = cast(input("Enter Number: "))
                num2 = cast(input("Enter Number: "))
                result = str(num1 / num2)
                print("==============================================================")
                print(f"  The Division of '{num1}' And '{num2}' is: '{result}'")
                print("==============================================================")
                file.write("\n"+str(num1) + " ÷ " + str(num2) + " = " + result + "\n")
                press()
            except ZeroDivisionError:
                print("\nAn Error has Occurred Due To Zero Division")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Get Factorial Of A Number
        elif user_input == "5":
            try:
                num = int(input("Enter A Number To Get Its Factorial: "))
                result = str(math.factorial(num))
                print("==================================")
                print(f"  The Factorial of '{num}' is:")
                print(f"==================================\n{result}")
                file.write(f"\n\nThe Factorial of {num} is:\n\t\t {result} \n\n")
                press()
            except (ValueError, TypeError):
                print(
                    "\nError: Factorial cannont Be Defined!")
                press()

        # To Get Squar Upto That Number
        elif user_input == "6":
            try:
                i = 1
                n = int(input("\nEnter Number To Get Square Upto That: "))
                file.write("\nHere is Square Root Upto: " + str(n) + "\n\n")
                while(i <= n):
                    file.write('\t' + (str(str(i) + " = " + str(i*i))) + "\n")
                    print(str(str(i)+"x"+str(i)+" = "+str(i*i)))
                    i = i+1
                file.write("\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # To Get Factorial Up To Entered Number
        elif user_input == "7":
            print("*****************************************************************")
            print(" WARNING: Enter Number Below 100 Don't Enter big Number\n If you have Big Number,Try Option 5.")
            print("*****************************************************************\n")
            try:
                n = int(input("Enter A Number To Find Factorial: "))
                if(n > 500):
                    print("\t\tYou Can Only Enter Upto 500!")
                    continue
                elif (n < 0):
                    print("Error: Factorial of Negitive Number is Not Defined")
                elif(n == 0):
                    print(1)
                else:
                    file.write("\n\n")
                    f = 1
                    for i in range(1, n+1):
                        x = ("Factorial "+str(i) + " = " + str(f)+"")
                        file.write("The Factorial of " + str(i) + " is: "+str(f)+"\n")
                        print(x)
                        f = f*i
                file.write("\n\n")
                press()
            except(ValueError, TypeError):
                print("\nError Occurred")
                press()

        # To Get Table Of Entered Number
        elif user_input == "8":
            try:
                i = 1
                n = cast(input("Enter Number To Get Its Table: "))
                print("========================")
                print(f"  Table of '{n}' is :")
                print("========================")
                file.write("\n\n Table of " + str(n) + " is:\n")
                while(i <= 10):
                    file.write("\t\t" + (str(str(n) + " x " + str(i) + " = " + str(i*n))) + "\n")
                    print("\t"+str(str(n)+"x"+str(i)+" = " + str(i*n)))
                    #print(f"{n} x {i} = {i*n}")
                    i = i+1
                file.write("\n\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Table Upto Entered Number
        elif user_input == "9":
            try:
                def generate_table(table_number, table_range):
                    for i in range(1, table_number + 1):
                        print(f"Table of {i} upto {table_range}:")
                        for j in range(1, table_range + 1):
                            result = j * table_range
                            print(f"{j} * {table_range} = {result}")
                        print("\n")

                def print_tables(file_path, table_number, table_range):
                    for i in range(1,table_number + 1):
                        file.write(f"Table of {i} upto {table_range}:\n")
                        for j in range(1, table_range + 1):
                            result = i * j
                            file.write(f"{i} * {j} = {result}\n")
                        file.write("\n")

                def main():
                    try:
                        user_number = int(input("Tables upto which number: "))
                        user_range = int(input("Enter the range for tables: "))
                    except ValueError:
                        print("Please enter valid numbers.")
                        return

                    generate_table(user_number, user_range)

                    file_path = "calculator.log"
                    print_tables(file_path, user_number, user_range)

                    print("=====================================================================================================")
                    print(f"Tables upto '{user_number}' with range upto '{user_range}' have been generated and saved to '{file_path}'.")
                    print("=====================================================================================================")

                if __name__ == "__main__":
                    main()
                press()
            except (ValueError, TypeError):
                print("\nError Occurred!")
                press()

        # To Get Cube of Number Upto Entered Number
        elif user_input == "10":
            try:
                i = 1
                n = int(input("Enter Number To Get Cube Upto That: "))
                file.write("\n\nHere is Cube Root Upto: " + str(n) + "\n\n")
                while(i <= n):
                    file.write("\t" + (str(str(i) + " = " + str(i*i*i))) + "\n")
                    print(str(str(i)+"x" + str(i) + "x" + str(i) + " = " + str(i*i*i)))
                    i = i+1
                press()
            except(ValueError, TypeError):
                print("\nError Occurred")
                press()

        # To Find Square Root of Entered Number
        elif user_input == "11":
            try:
                n = cast(input("Enter a Number To Find Square Root: "))
                #result = str(math.sqrt(num1))
                print("===============================================")
                print("  Square Root of " + str(n) + " is: " + str((n**(1/2))))
                print("===============================================")
                file.write("\n Square Root Of "+str(n) + "² is: " + str((n**(1/2))) + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # To Find Cube Root Of Entered Number
        elif user_input == "12":
            try:
                n = cast(input("Enter Number To Find Cube Root of: "))
                print("==================================================")
                print("  Cube Root of " + str(n)+" is: " + str((n**(1/3))))
                print("==================================================")
                file.write("\n Cube Root of " + str(n) + "³ is: " + str((n**(1/3))) + "\n")
                press()
            except(ValueError, TypeError):
                print("\nError Occurred")
                press()

        # To Get All Prime Numbers Between Entered Number
        elif user_input == "13":
            try:
                l = int(input('Enter Lower Range: '))
                u = int(input('Enter Upper Range: '))
                if(l > u):
                    l = l+u
                    u = l-u
                    l = l-u
                file.write(f"\n\nPRIME NUMBERS Between {l} And {u} Are:\n")
                print("\n=========================================")
                print(f" PRIME NUMBERS Between '{l}' And '{u}' Are:")
                print("=========================================\n")
                for num in range(l, u+1):
                    if num > 1:
                        for i in range(2, num):
                            if(num % i) == 0:
                                break
                        else:
                            print(str(num), end=" ")
                            file.write(str(num)+" ")
                print()
                file.write("\n")
                press()
            except(ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Raises a Number To The Power of Another
        elif user_input == "14":
            try:
                num1 = cast(input("Enter Number: "))
                num2 = cast(input("Enter Number: "))
                result = str(num1**num2)
                print("\n====================================================")
                print(f"  Power of '{num1}' and '{num2}' is: '{result}'")
                print("====================================================")
                file.write("\n"+str(num1) + " ** " + str(num2) + " = " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError Occurred")
                press()

        # Calculates Percentage of a Number
        elif user_input == "15":
            try:
                num1 = cast(input("Enter Number To Find Percentage: "))
                result = str(num1 / 100)
                print("\n==================================================")
                print(f"  Percentage : '{result}'")
                print("==================================================")
                file.write("\n"+str(num1) + " %  = " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError occurred")
                press()

        # Finds The Sine of a Number
        elif user_input == "16":
            try:
                num = cast(input("Enter Number: "))
                result = str(math.sin(num))
                print("\n==================================================")
                print(f"  Sine '{num}' is: '{result}'")
                print("==================================================")
                file.write("\n Sin "+str(num) + " is: " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError occurred")
                press()

        # Finds The Cosine of a Number
        elif user_input == "17":
            try:
                num = cast(input("Enter Number: "))
                result = str(math.cos(num))
                print("\n==================================================")
                print(f"  Cosine '{num}' is: " + result)
                print("==================================================")
                file.write("\n Cos "+str(num) + " is: " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError occurred")
                press()

        # Finds The Tangent of a Number
        elif user_input == "18":
            try:
                num = cast(input("Enter a number: "))
                result = str(math.tan(num))
                print("\n==================================================")
                print(f"  Tangent '{num}' is: " + result)
                print("==================================================")
                file.write("\n Tan "+str(num) + " is: " + result + "\n")
                press()
            except (ValueError, TypeError):
                print("\nError occurred")
                press()

        # ABOUT INFO
        elif user_input == "19":
            print(
                "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(
                "\n\tWelcome to Ancod3r's Calculator \tVersion " + version + "\n\tHere you can do many types of mathematical operations\n\tBest for std' who wants to learn/memorize\n\tPrograms for finding squar root, cube root, tables and many more.\n\tEvery operation you make are saved in 'calculator.log' File.\n\tNew Version and GUI interface comming soon.\n\tWith some more advance features\n\tTill then enjoy this calcultor...\n\tFor any query or suggession contact me on\nEmail - abcdany@gmail.com\nWhatsApp - +91987654321")
            print(
                "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            press()

        # Exits The User From The Calculator
        elif user_input.lower() == "quit" or user_input.lower() == "q":
            print(
                "\n*************************************************************************")
            print(
                "\t\tThank You For Using This Calculator !\n\t\t Made By RAJNEESH")
            print(
                "*************************************************************************")
            print('Exiting. . .')
            break

        # Displayed For Unknown Input
        else:
            print("\n==========================")
            print("     Unknown Input")
            print("==========================")
            press()
        # Displays the options for the user
        options()
if __name__ == "__main__":
    calculator()
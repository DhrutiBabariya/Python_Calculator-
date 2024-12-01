import pyttsx3
engine = pyttsx3.init()

def calculator():
    print("\"Welcome To The Python Calculator\"")
    engine.say("\"Welcome To The Python Calculator\"")
    engine.runAndWait()

    while True:
        print(" \nThe Operations :")
        print("1. SUM (+)  ")
        print("2. DIFFERENC (-)  ")
        print("3. MULTIPLICATION (*)  ")
        print("4. DIVITION (/)  ")
        print("5. SQUARE (2)")
        print("6. CUBE (3)")
        print("7. EXIT the calculator")
        
        engine.say("Enter Your Choice")
        engine.runAndWait()
        Choice=input("\nEnter Your Choice [+, -, *, /, 2, 3]  or 'e'(for Exit) : ")

        if Choice=="e":
            print("Exiting The Calculator...")
            engine.say("Exiting The Calculator ")
            engine.runAndWait()
            break
            
        if Choice not in ["+", "-", "*", "/", "2", "3"]:
            print("Please Enter Valid Operation!!")
            continue
            engine.say("Please Enter Valid Operation")
            engine.runAndWait()
        
        if Choice=="2" or Choice=="3":
            try:
                Number=float(input("Enter A Number : "))

                if Choice=="2":
                    engine.say("YOUR ANSWER : ")
                    engine.runAndWait()
                    print(f"SQUARE OF {Number} = ",Number**2)
                    
                if Choice=="3":
                    engine.say("YOUR ANSWER : ")
                    engine.runAndWait()
                    print(f"CUBE OF {Number} = ",Number**3)
            except ValueError:
                print("Please, Enter Valid Number!!")
                engine.say("Please, Enter Valid Number")
                engine.runAndWait()
        else :
            try:
                n1=float(input("Enter First Number : "))
                n2=float(input("Enter Second Number : "))

                if Choice=="+":
                    engine.say("YOUR ANSWER : ")
                    engine.runAndWait()
                    print(f"ANSWER : {n1} + {n2} = ",n1+n2)

                elif Choice=="-":
                    print(f"ANSWER : {n1} - {n2} = ",n1-n2)
                    engine.say("YOUR ANSWER : ")
                    engine.runAndWait()
                    
                elif Choice=="*":
                    print(f"ANSWER : {n1} * {n2} = ",n1*n2)
                    engine.say("YOUR ANSWER : ")
                    engine.runAndWait()
                    
                else:
                    if n2==0 :
                        print("CAN NOT DIVIDE BY ZERO!!")
                        engine.say("CAN NOT DIVIDE BY ZERO ")
                        engine.runAndWait()
                    else:
                        print(f"ANSWER : {n1} / {n2} = ",n1/n2)
                        engine.say("YOUR ANSWER : ")
                        engine.runAndWait()
            except ValueError:
                print("Please, Enter Valid Number!!")
                engine.say("Please, Enter Valid Number")
                engine.runAndWait()    
calculator()

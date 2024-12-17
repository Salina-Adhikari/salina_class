f_1=int(input("Enter the first number:"))
f_2=int(input("Enter second number:"))
user_choice=input("""
          Please choose option 
                  * for multiplication
                  - for subtraction  
                      
                  
                  """)
if user_choice=="*":
    print("Multiplaction= ",f_1*f_2)
elif user_choice=="-":
    print("Subtraction= ",f_1-f_2)
else :
    print("Invalid choice")


Number=int(input("Enter the square root of a Number:"))
Guess=int(input("Enter the Guessed Number:"))
#Condition
while(True):
    Factorial_of_Number=Guess*Guess-Number
    Derivative_of_Number=2*Guess
Generated_root=Guess-(Factorial_of_Number/Derivative_of_Number)
print(Generated_root)
Guess=Generated_root
break





                                                                                                                                                                                         OUTPUT:
     


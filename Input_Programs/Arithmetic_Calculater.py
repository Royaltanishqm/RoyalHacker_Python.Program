Num1=input("Enter First Number: ")
Num2=input("Enter Second Number: ")
whichAR=input("Enter which Arithmetic Operation you want to perform (+, -, *, /, %): ")
if whichAR=="+":
    print("Addition: ", int(Num1)+int(Num2))
elif whichAR=="-":
    print("Subtraction: ", int(Num1)-int(Num2))
elif whichAR=="*":
    print("Multiplication: ", int(Num1)*int(Num2))
elif whichAR=="/":
    print("Division: ", int(Num1)/int(Num2))
elif whichAR=="%":
    print("Modulus: ", int(Num1)%int(Num2))
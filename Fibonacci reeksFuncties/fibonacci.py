def fibionaccifunction(amount):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(amount):
        fibionacci = num1+num2
        num1=num2
        num2=fibionacci
        print(fibionacci)

fibionaccifunction(11)
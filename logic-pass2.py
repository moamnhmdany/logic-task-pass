def findPrimeNumbers(number1:int , number2:int):
    
    for initialNumber in range(number1,number2 + 1):
        if initialNumber > 1:
            for num in range(2,initialNumber):
                if (initialNumber % num) == 0:
                    break
            else:
                print(initialNumber)     

findPrimeNumbers(1,6)
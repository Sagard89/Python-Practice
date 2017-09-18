def calculateSquares(limit):
    initialNumber = 1
    for i in range(limit):
        if(initialNumber==1):
            initialNumber = initialNumber + 1
            print(initialNumber)
        else:
            initialNumber = initialNumber ** 2
            print(initialNumber)
    print(initialNumber)

calculateSquares(10)

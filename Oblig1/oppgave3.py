print("skriv første tall")
firstNumber = int(input())
#if firstNumber == <class ’int’>:
    print("skriv andre tall")
    secondNumber = int(input())
#    if secondNumber == int:
        gange = firstNumber * secondNumber
        dele = firstNumber / secondNumber
        pluss = firstNumber + secondNumber
        minus = firstNumber - secondNumber
        modulo = firstNumber % secondNumber
        opphoye = firstNumber ** secondNumber
        deleNedrunde = firstNumber // secondNumber
        print("Resultater")
        print(firstNumber, "ganget med", secondNumber, "=", gange)
        print(firstNumber, "delet på", secondNumber, "=", dele)
        print(firstNumber, "pluss", secondNumber, "=", pluss)
        print(firstNumber, "minus", secondNumber, "=", minus)
        print(firstNumber, "modulo", secondNumber, "=", modulo)
        print(firstNumber, "opphøyet i", secondNumber, "=", opphoye)
        print(firstNumber, "delt på", secondNumber, "rundet ned =", deleNedrunde)
#    else: print("ikke gjyldig verdi prøv igjen")
#else: print("ikke gjyldig verdi prøv igjen")

#fix måte å sjekke om inputvalue er int eller ikke
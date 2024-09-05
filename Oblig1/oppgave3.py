print("skriv første tall")
firstNumber = float(input())#skriv inn en tall verdi
print("skriv andre tall")
secondNumber = float(input())

gange = firstNumber * secondNumber#regner ut gange osv.
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
print(firstNumber, "modulus", secondNumber, "=", modulo)
print(firstNumber, "opphøyet i", secondNumber, "=", opphoye)
print(firstNumber, "delt på", secondNumber, "rundet ned =", deleNedrunde)
#koden skriver ut alle utregningene gjort fra linje 6-12
#bruker for kommandoen til å skrive en liste med oddetall fra 9 til 101
TALL = range(9, 101)
for x in TALL:
    if (x % 2) == 0 : #hvis tall i x delt på to har null i rest hopp over tallet, dermed vil programmet ikke printe partall.
        continue
    print(x)

#bruker while til å lage en oddetalls liste fra 9 til 101
y = 7
while y < 101:
    y = y + 2
    print(y)
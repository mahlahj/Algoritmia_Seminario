numero =  int(input("n: "))
e = 0

for i in range (numero):
    j = i
    factorial = 1
    while j > 0:
        factorial = factorial * j
        j -= 1

    e = e + 1/factorial
    print(e)
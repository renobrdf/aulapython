def myPi(n):
    denominador = 1
    soma = 1

    for i in range(n):
        denominador = denominador + 2
        soma = soma - (1/denominador)
        denominador = denominador + 2
        soma = soma + (1/denominador)

    pi = soma * 4

    return(pi)

print(myPi(1000000))


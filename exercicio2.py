n1=int(input("Coloque um número"))
n2=int(input("Coloque outro número"))
print('''[ 1 ] somar 
[ 2 ] subtrair 
[ 3 ] multiplicar
[ 4 ] dividir''')
op =int(input("Escolha a operação: "))
if op == 1:
  soma = n1+n2
  print("A soma entre {} + {} é {}".format(n1,n2,soma))
elif op ==2:
  subtrair = n1-n2
  print("A subtração entre {} - {} é {}".format(n1,n2,subtrair))
elif op ==3:
  multiplicar = n1*n2
  print("A multiplicação entre {} x {} é {}".format(n1,n2,multiplicar))
elif op ==4 :
  dividir = n1/n2
  print("A divisão entre {} / {} e {}".format(n1,n2,dividir))
    


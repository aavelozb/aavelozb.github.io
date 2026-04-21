# def mifuncion(x):
#    y = 2*x+3
#    print(y)
#    return y
# a = 5
# print(a, mifuncion(a))


# from math import sqrt
# def distancia(x1, y1, x2, y2):
#    return sqrt((x1-x2)**2 + (y1-y2)**2)
# a = float(input('Coordenada x del primer punto: '))
# b = float(input('Coordenada y del primer punto: '))
# c = float(input('Coordenada x del segundo punto: '))
# d = float(input('Coordenada y del segundo punto: '))
# dist = distancia(a,b,c,d)
# print('La distancia es: ', dist)


# def factorial(n):
#    if n == 0 or n == 1:
#       return 1
#    cont = 2
#    f = 1
#    while cont <= n:
#       f *= cont
#       cont += 1
#    return f

# def coef_binomial(n, k):
#    fn = factorial(n)
#    fk = factorial(k)
#    fnmk = factorial(n-k)
#    return fn / (fk*fnmk)


# def factorial(n):
#    if n == 0 or n == 1:
#       return 1
#    cont = 2
#    f = 1
#    while True:
#       f *= cont
#       cont += 1
#       if cont == n:
#          return f*n



# def num_digitos(n):
#    cont = 0   
#    while n>0:
#       n = n//10
#       cont += 1
#    return cont
# print(num_digitos(12345))   

def invertir_numeros(n):
   cont = 0
   while n>0:
      n = n//10
      cont += 1
   return cont



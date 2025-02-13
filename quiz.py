# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
print("------------------------------")
a=float(input("Digite su valor: "))
b=float(input("Digite su valor: "))
c=float(input("Digite su valor:"))
print("------------------------------")

#processing 
if a + b > c:
    #Output
    print("Si")
elif c + b > a:
    print("Si")
elif c + a < b:
    print("Si")
else:
    print("No")    
pass

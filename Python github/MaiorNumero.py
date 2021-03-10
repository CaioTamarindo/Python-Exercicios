for i in range (5):
    if i==0:
        a=int(input("Digite um numero: "))
        x=a
        continue

    a=int(input("Digite um numero:"))
    if a>x:
        x=a
    

print("O maior numero é: ", x)
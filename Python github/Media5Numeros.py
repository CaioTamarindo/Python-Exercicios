for i in range (5):
    if i==0:
        a=int(input("Digite um numero:"))
        soma=a
        continue

    a=int(input("Digite um numero:"))
    soma+=a

media=soma/5
print("A soma é igual a: ",soma," e a media igual a: ", media )
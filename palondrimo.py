# frase = input("ingrese frase: ")
# res = frase[::-1]

# if frase == res:
#     print("This word is a palindrome")
# else:
#     print("This word is not a palindrome")

# print("palabra: " + res)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_pares = []
lista = []
for pares in a:
    if pares % 2 == 0:
        lista_pares.append(pares)
print(lista_pares)

# números = []
# for x in range(1,101):
#     números.append(x)
# print(números)
# print("-----------------------------")
# #lista en reversa
# números.reverse()
# print(números)

lista = [1,2,3,4,5]
res = []
for i in lista:
    inversa = [lista[-i]]
    print(inversa) 
    res.append(inversa[0])
print(res)
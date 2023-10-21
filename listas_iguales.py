# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 21, 10, 11, 12, 13]

# num_repetidos = []
# for x in a:
#     for y in b:
#         if [x] == [y]:
#             # print('si hay elementos iguales')
#             num_repetidos.append(x)

# print(num_repetidos)
# print(num_repetidos[1:])

# print(set(a).intersection(set(b))) -> función de intersección

# Lista para obtener el numero repetido
myList = [1, 8, 9.8, 8, 10]

res = []
print(len(myList))

for n in range(len(myList)):
    for r in range(len(myList)):
        if n != r:
            if myList[n] == myList[r] and myList[n] not in res:
                res.append(myList[n])
                print(res)

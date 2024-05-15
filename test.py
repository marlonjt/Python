# T = int(input())
# for _ in range(T):
#     S = input()
#     print(S[0::2] + " " + S[1::2])

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

# print(" ".join(map(str, arr[::-1])))

print(n)
print(arr)
[print(i, end=" ") for i in arr[::-1]]

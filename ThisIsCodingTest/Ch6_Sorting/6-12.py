
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A, reverse=False)
sorted_B = sorted(B, reverse=True)

maximum = -1
for t in range(K):
    if sum(sorted_A) < maximum:
        break
    else:
        maximum = sum(sorted_A)
    if sorted_A[t] < sorted_B[t]:
        sorted_A[t], sorted_B[t] = sorted_B[t], sorted_A[t]

print(sum(sorted_A))
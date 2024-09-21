def backtrack(A, index, subsequence, aux, max_val):
    # Caso base: si ya procesamos todos los anillos de A
    if index == len(A):
        return max(max_val, aux)
    
    # Excluimos el anillo en la posición actual
    max_val = backtrack(A, index + 1, subsequence, aux, max_val)
    
    # Incluimos el anillo en la posición actual si forma una secuencia valida
    if len(subsequence) == 0 or (len(subsequence) > 0 and subsequence[len(subsequence)-1][0] < A[index][1]):
        subsequence.append(A[index])
        max_val = backtrack(A, index + 1, subsequence, aux + A[index][2], max_val)
        subsequence.pop()
    
    return max_val

# Lectura de entrada
t = int(input())
A = []
for _ in range(t):
    a, b, h = map(int, input().split())
    ring = (a, b, h)
    A.append(ring)

A.sort(key=lambda x: (x[1], x[0]), reverse=True)
max_val = 0
max_val = backtrack(A, 0, [], 0, max_val)
print(max_val)
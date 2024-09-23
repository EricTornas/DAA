def _backtrack(S, index, subsequence, aux, T):
    # Caso base: si ya procesamos todos los enteros de S
    if index == len(S):
        return T == aux
    
    # Excluimos el elemento en la posición actual
    x = _backtrack(S, index + 1, subsequence, aux, T)
    
    # Incluimos el elemento en la posición actual 
    subsequence.append(S[index])
    y = _backtrack(S, index + 1, subsequence, aux + S[index], T)
    subsequence.pop()
    
    return x or y

def backtrack(S, T):
    return _backtrack(S, 0, [], 0, T)

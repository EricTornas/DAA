def subset_sum_dp(S, T):
    dp = [False] * (T + 1)
    dp[0] = True  # La suma 0 siempre es alcanzable
    
    for s in S:
        # Recorremos en orden inverso
        for j in range(T, s - 1, -1):
            if dp[j - s]:
                dp[j] = True
    
    return dp[T]
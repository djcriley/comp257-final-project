
def dp_maxFundableSubset(Q, F, budget):
    # Initialize the dp array with zeros
    n = len(Q)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Iterate over the proposals and the budgets
    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if F[i - 1] <= j:
                # If we can fund the proposal, we can either fund it or not fund it
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - F[i - 1]] + Q[i - 1])
            else:
                # If we can't fund the proposal, we can only not fund it
                dp[i][j] = dp[i - 1][j]

    # Initialize the list of funded proposals with an empty list
    maxFundableSubset = []

    # Iterate over the proposals and the budgets in reverse order
    i = n
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            # If we didn't fund the proposal, move to the previous proposal
            i -= 1
        else:
            # If we funded the proposal, add its index to the list of funded proposals
            maxFundableSubset.append(i - 1)
            # Decrease the budget by the amount of funding requested
            j -= F[i - 1]
            # Move to the previous proposal
            i -= 1

    # Reverse the list of funded proposals to get the correct order
    maxFundableSubset.reverse()

    
    return maxFundableSubset

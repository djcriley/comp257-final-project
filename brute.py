
def brute_maxFundableSubset(Q, F, budget):
    # Generate all possible subsets of the proposals
    n = len(Q)
    subsets = [[]]
    for i in range(n):
        subsets += [subset + [i] for subset in subsets]

    # Initialize the maximum total quality with zero
    maxTotalQuality = 0

    # Initialize the list of funded proposals with an empty list
    maxFundableSubset = []

    # Iterate over the subsets and select the one with the maximum total quality
    for subset in subsets:
        # Calculate the total quality and total funding of the current subset
        totalQuality = sum([Q[i] for i in subset])
        totalFunding = sum([F[i] for i in subset])

        if totalFunding <= budget and totalQuality > maxTotalQuality:
            # If the subset fits within the budget and has a higher total quality, update the maximum total quality and the list of funded proposals
            maxTotalQuality = totalQuality
            maxFundableSubset = subset

    
    return maxFundableSubset

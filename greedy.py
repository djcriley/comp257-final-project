
def greedy_maxFundableSubset(Q, F, budget):
    # Create a list of tuples (quality, funding, index)
    proposals = [(q, f, i) for i, (q, f) in enumerate(zip(Q, F))]

    # Sort the proposals by funding in descending order
    proposals.sort(key=lambda x: x[0]/x[1], reverse=True)

    # Initialize the list of funded proposals with an empty list
    maxFundableSubset = []

    # Iterate over the proposals and select the ones with the highest quality-to-funding ratio
    for proposal in proposals:
        if proposal[1] <= budget:
            # Add the proposal to the list of funded proposals
            maxFundableSubset.append(proposal[2])
            # Decrease the budget by the amount of funding requested
            budget -= proposal[1]
    
    maxFundableSubset.sort()
    
    return maxFundableSubset




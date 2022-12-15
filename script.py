
import random

import timeit

from brute import brute_maxFundableSubset
from dp import dp_maxFundableSubset
from greedy import greedy_maxFundableSubset

# Function to generate random input
def random_input(n):
    # Generate random quality ratings and funding requests
    Q = [random.randint(1, 100) for _ in range(n)]
    F = [random.randint(1, 100) for _ in range(n)]
    # Use a random budget that is at least as large as the total funding requested
    budget = random.randint(1, sum(F))
    return (Q, F, budget)

# Function to generate random input of increasing size
def input_sizes():
    for n in [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
        yield random_input(n)

# Function to time the greedy algorithm
def time_greedy():
    # Define the function to be timed
    def run_greedy():
        
        return greedy_maxFundableSubset(Q, F, budget)

    # x = run_greedy()
    # verify_cost = 0
    # verify_quality = 0
    # for index in x:
    #     verify_cost += F[index] 
    #     verify_quality += Q[index]
    

    # print(f"Greedy - Total Funding used: {verify_cost}, Total Quality: {verify_quality}, Subset: {x}")
        
    # Time the function using the timeit module
    time = timeit.timeit(run_greedy, number=1)
    return time

# Function to time the dynamic programming algorithm
def time_dp():
    # Define the function to be timed
    def run_dp():
        return dp_maxFundableSubset(Q, F, budget)
        

    # x = run_dp()
    # verify_cost = 0
    # verify_quality = 0
    # for index in x:
    #     verify_cost += F[index] 
    #     verify_quality += Q[index]


    # print(f"DP - Total Funding used: {verify_cost}, Total Quality: {verify_quality}, Subset: {x}")
    # Time the function using the timeit module
    time = timeit.timeit(run_dp, number=1)
    return time

# Function to time the brute force algorithm
def time_brute_force():
    # Define the function to be timed
    def run_brute_force():
        return brute_maxFundableSubset(Q, F, budget)

    # x = run_brute_force()
    # verify_cost = 0
    # verify_quality = 0
    # for index in x:
    #     verify_cost += F[index] 
    #     verify_quality += Q[index]

    # print(f"Brute - Total Funding used: {verify_cost}, Total Quality: {verify_quality}, Subset: {x}")
    # Time the function using the timeit module
    time = timeit.timeit(run_brute_force, number=1)
    return time

def print_testcases(Q, F):
    proposals = [(q, f, i) for i, (q, f) in enumerate(zip(Q, F))]
    
    for proposal in proposals:
        print(f"{proposal[2]}, {proposal[0]}, {proposal[1]}")


with open("DPvsGreedy.csv", "w") as output:

    # print("Input size, Greedy, DP, Brute force", file=output)
    for (Q, F, budget) in input_sizes():
        # print(f"{len(Q)},{time_greedy()},{time_dp()}", file=output)
        print("-----------------------")
        print(f"Index, Quality, Funding, budget = {budget}, n = {len(Q)}")
        # print_testcases(Q, F)
        # print(f"{len(Q)},{time_greedy()},{time_dp()}, {time_brute_force()}", file=output)
        print(f"{len(Q)},{time_greedy()},{time_dp()}", file=output)

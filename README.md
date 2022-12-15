# comp257-final-project


This project was split up into seperate files:

- brute.py has the brute force implementation 
- dp.py has the dynamic programming implementation
- greedy.py has the greedy implementation 
- script.py is used to run all functions and time them, then output them to a CSV file
- graph.py is used to make the graphs shown below
- output.csv contains results from running all 3 implementation 
- DPvsGreedy.csv contains results from running DP and greedy implentations on larger input sizes to get a closer look at runtime comparison
- result.txt shows the results of the algorithms run 2 times on input sizes 5, 10, 15, 20, 25



## Runtimes

Greedy: O(n log n)
Dynamic Programming: O(n)
Brute Force: O(2^n)

## Test cases
I used random test cases of verious lengths to test the algorithms. In order to check the correctness of the DP and greedy algorithm I could compare it to the brute force as it is garunteed the correct answer if given enough time to run. 

I only ran all 3 algorithms on smaller imput sizes up to 25 because anything higher brute force would exceed 3 minute runtimes and cause segmentation faults due to no more memory left on my computer. 

I proceeded to run DP vs greedy on larger input sizes [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] in order to see how they compare on the largest input sizes

It was found that the greedy implementation outperformed the dynamic programming implementation on all input sizes, but was not always garunteed the correct output.

## Why Greedy Does Not Always Give Correct Output
Since my greedy implementation used the ratio of quality/cost in order to sort the proposals, it can sometimes lead to a non-optimal answer. We can see this happen on this test case:
-----------------------
Index, Quality, Funding, budget = 101, n = 5
0, 3, 29
1, 52, 58
2, 40, 27
3, 8, 47
4, 44, 33
Greedy - Total Funding used: 89, Total Quality: 87, Subset: [0, 2, 4]
DP - Total Funding used: 91, Total Quality: 96, Subset: [1, 4]
Brute - Total Funding used: 91, Total Quality: 96, Subset: [1, 4]

This shows a moment when the greedy algorithm can sometimes get a non-optimal soltuon. THis is because it sorts based on quality/cost ratio, making it select the proposals that are the most "worth it" but since it is greedy it will always select a proposal if it fits. If it does not fit then it doesnt chose it, but sometimes selecting the first proposals might not be the optimal subset.


## Recomendation
I would chose the greedy algorithm due to it returning the correct answer for almost all test cases while also having the fastest theoritical runtime. For garunteed results i would use the dynamic programming approach to get the correct optimal solution and although it has the fastest theoritical runtime, the experimental runtime did not match up this is most likely because of my computer

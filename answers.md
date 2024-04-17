# CMPS 2200 Assignment 3
## Answers

**Name:** Nicolas Labarca


Place all written answers from `assignment-03.md` here for easier grading.


1a) To minimize the number of coins needed to sum up to n dollars, one should employ a greedy algorithm by repeatedly selecting the largest available coin denomination that does not exceed n. Start with the highest value of k for which 2^k is less than or equal to n, then reduce n by this coin value and continue until n is zero. This method focuses on taking the maximum allowable amount of the largest possible denomination at each step.

1b) This approach is optimal because it leverages a greedy method, consistently opting for the largest denomination 
2^k that is feasible, before considering smaller denominations. By choosing the largest possible coins first, the algorithm reduces the total number of coins required to reach the amount. This technique ensures that the solution to the newly reduced problem (after selecting the largest coin) is tackled optimally, thereby maximizing the reduction in coin count at every step and optimizing the solution throughout.

1c) Both the work and the span of this algorithm are O(logn), reflecting the logarithmic number of decisions needed to break down the original amount using progressively smaller denominations.

2a) Consider a situation where the coin denominations in Fortuito are 1, 3, and 4, and the target amount is 6. Applying a greedy algorithm might lead to choosing the 4-dollar coin first, leaving 2 dollars to be covered by two 1-dollar coins. This results in a total of three coins. However, a more efficient solution would utilize two 3-dollar coins, achieving the target with only two coins, thereby demonstrating that the greedy method may not always yield the least number of coins.

2b) The principle of optimal substructure in this context means that the best way to assemble the needed amount is by building on the optimal solutions for smaller amounts. This property is evident as the minimum number of coins needed to construct any amount up to n can be methodically calculated using a dynamic approach, by incrementally building from the solution of smaller subproblems.

2c) The computational effort or work for the dynamic programming solution is O(nk), where n is the target amount and k is the number of different denominations available. The span, representing the longest sequence of dependent operations, is O(n), assuming each subproblem is solved sequentially.

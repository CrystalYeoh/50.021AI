I experimented on the following solution methods:
- Pure backtracking
- Minimum remaining values
- Least constraining value
- Both MRV and LCV
- Backtracking with forward checking
- Backtracking with forward checking, mrv, lcv
- Backtracking with AC3
- Backtracking with AC3, mrv, lcv

The results were that given the current order of processing the variables, all configurations did well and only took the minimum of 9 assignments to complete the question.

To make the results comparable and see differences in the solutions, I varied the order of processing the CSP variables by calling `random.shuffle(csp_vars)`, and ran each solution for 100 times (to be solved 100 times, each time the order of the variables are shuffled), and took the worst performance from there.

Now we can see a much distinct difference between the different solutions.
```bash
Pure backtracking
44
Backtracking with Minimum Remaining Values
44
Backtracking with Least Constraining Value
53
Backtracking with both MRV and LCV
32
Backtracking with Forward checking
24
Backtracking with Forward checking, MRV, LCV
9
Backtracking with AC3
15
Backtracking with AC3, MRV, LCV
9
```

As a rule of thumb, forward checking always seem to do better than pure back tracking, and AC3 algorithm is always capped at 15 assignments max. This is to be expected as forward checking would not do worse then pure back tracking as it only deletes away illegal values by checking forward. Similarly, for AC3 it does not do worse than forward checking because it is able to detect more illegal values early on.

However, what seems to be more effective is either forward checking or AC3, coupled with MRV and LCV. This is probably due to the order of processing the variables, and with the combination of both MRV and LCV, the algorithm is able to choose the most efficient order of processing the variables without being affected by the random order.

Additionally, choosing the variables with the least constraining value consistently seems to be perform worse for this solution, probably as it directs the algorithm away from the solution instead.
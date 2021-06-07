import pdb
from csp import *
from random import shuffle

def solve_semi_magic(algorithm = backtracking_search,**args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d'%d for d in range(1,10)]

    #########################################
    # Fill in these definitions

    csp_domains = {x:[1,2,3] for x in csp_vars}
    csp_neighbors = {'V1':['V2','V3','V4','V7','V5','V9'],
                    'V2':['V1','V3','V5','V8'],
                    'V3':['V1','V2','V6','V9'],
                    'V4':['V1','V7','V5','V6'],
                    'V5':['V2','V8','V4','V6','V1','V9'],
                    'V6':['V4','V5','V3','V9'],
                    'V7':['V1','V4','V8','V9'],
                    'V8':['V2','V5','V7','V9'],
                    'V9':['V1','V5','V7','V8','V3','V6']}


    def csp_constraints(A, a, B, b):
        # Doesn't matter which variable, since all the constraints are just whether variables are diff
        return a!=b

    #########################################
    
    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)


    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)
    print("Number of assignments:", csp.nassigns,"\n")


    # print('number of assignments', csp.nassigns)
    # assign = csp.infer_assignment()
    # if assign:
    #     for x in sorted(assign.items()):
    #         print(x)
    # return csp


# Pure backtracking
print("Pure backtracking")
solve_semi_magic()

# Minimum remaining values
print("Backtracking with Minimum Remaining Values")
solve_semi_magic(select_unassigned_variable= mrv)

# Least constraining value
print("Backtracking with Least Constraining Value")
solve_semi_magic(order_domain_values= lcv)

# Both MRV and LCV
print("Backtracking with both MRV and LCV")
solve_semi_magic(select_unassigned_variable= mrv, order_domain_values= lcv)

# Backtracking with forward checking
print("Backtracking with Forward checking")
solve_semi_magic(inference = forward_checking)

# Backtracking with forward checking, mrv, lcv
print("Backtracking with Forward checking, MRV, LCV")   
solve_semi_magic(inference = forward_checking,select_unassigned_variable= mrv, order_domain_values= lcv)

# Backtracking with AC3
print("Backtracking with AC3")
solve_semi_magic(inference = mac)
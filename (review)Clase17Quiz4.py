#
# For this problem, we would like you to implement pre-processing
# rules for SAT. We're going to use the same format as in the problem
# set for Unit 2 to represent Boolean Formulas (in conjunctive normal
# form):
#
# The number of variables will be given as an integer num_variables
# (all variables are consecutively numbered from 1 to (num_variables)
#
# The clauses will be represented as a list of lists called
# "clauses". The "outer list" contains all clauses, each inner list is
# a clause. The variable x_i is represented as i if it appears without
# a not, otherwise it is represented as -i
#
# For example, the Boolean Formula (x1 or x2 or not(x3)) and (x2 or
# not(x4)) and (not(x1) or x3 or x4) would translate into
#
# num_variables = 4
#
# clauses = [[1,2,-3],[2,-4],[-1,3,4]]
#
# For this exercise, please write a function that, when given a
# Boolean Formula in the above format, performs the following data
# reduction rules and outputs the resulting set of clauses:
#
# 1) If any clause consists of a single variable, set the variable so
# that this clause is satisfied
#
# 2) If a variable appears just once (and it hasn't been set, see
# below), set it so that the respective clause is satisfied
#
# 3) Remove all clauses that have become satisfied
#
# 4) Remove all variables that evaluate to 'FALSE' (i.e., all variables x
# that are set to FALSE and all variables not(x) where x is set to TRUE).
# If this results in an empty clause, then the input formula has no satisfying
# assignment and the function should return the Boolean formula [[1,-1]]
#
# The challenging part is implementing Rule 2, for your function must
# perform the data reductions exhaustively, that is, until they can no
# further be applied: After rules 2, 3 and 4 have been applied, there
# might be other clauses for which rule 2 now becomes applicable (you
# will have to be careful if a variable that now appears once has
# already been set earlier - if not, then Rule 2 may apply, otherwise
# it doesn't).
#
# Remember that pre-processing cannot change the satisfiablity. If
# a SAT problem is satisfiable, the output of the pre-processing also
# needs to be satisfiable.
#
# If through the pre-processing steps you are able to determine that a
# SAT problem is satisfiable then return []. Likewise, if you
# determine that it is unsatisfiable then return [[1,-1]]. Otherwise,
# return the remaining clauses.

def sat_preprocessing(num_variables, clauses):
    # YOUR CODE HERE
    rules_applicable = True
    temp_assignment = [None]*(num_variables+1)
    while rules_applicable == True:
        rules_applicable = False
        
        variable_counter = [0]*(num_variables-1)
        var_setting = [None]*(num_variables+1)
        
        for clause in clauses:
            for var in clause:
                avar = abs(var)
                variable_counter[avar] +=1
                var_setting[avar] = 1 (1 if var>0 else 0)
        
        for i, var in enumerate(variable_counter):
            if var !=1:
                continue
            if temp_assignment is not None:
                continue
            temp_assignment[i] = var_setting[i]
            
        for clause in clauses:
            assert len(clause) != 0
            if len(clause) >1:
                continue
            var = clause[0]
            avar = abs(var)
            
            if temp_assignment[avar] is not None:
                if temp_assignment[avar] != (1 if var>0 else 0) :
                    break
                  ##to review  
    


def test():
    assert [] == sat_preprocessing(1, [[1]])
    assert [[1,-1]] == sat_preprocessing(1, [[1], [-1]])
    assert [] == sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                         [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                         [1, 3, -4], [3, -4, 1], [-1]])
    assert [[1,-1]] == sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                         [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                         [-3, -1], [-4], [4, -1, 2]])
    ans = [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], [-3, 2, -5, 6, -4]])


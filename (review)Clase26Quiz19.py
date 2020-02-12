# The code below has been supplied so that you can see for
# yourself the various numbers of iterations for different
# inputs to the program.

def collatz(x):
    count = 0
    while x != 1:
        count = count + 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        print x
    print "Total number of iterations", count
    
# Please assign the variable iterations to a list of the
# number of iterations, in order, for the inputs 
# 6, 11, 27, 32 and 33.

# Do not change the variable name or your code will be 
# graded as incorrect.

iterations = [6, 11, 27, 32 , 33] # enter your values in the list.
for a in iterations:
    collatz(a)
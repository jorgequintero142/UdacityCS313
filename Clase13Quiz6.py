#
# Write a function that returns True if the
# input graph is 3-colorable.
#
# You're given a magical function, graph_is_4colorable
# that will return True if the input graph is
# 4-colorable and False otherwise.
#

from fourcolor import graph_is_4colorable

def graph_is_3colorable(g):
    # YOUR CODE HERE
    h = []
    for node in g:
        nn = node + [1]
        h.append(nn)
    h.append([1]*(len(g)+1))    
    return graph_is_4colorable(h)

def test():
    g1 = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
    assert graph_is_3colorable(g1)

    g2 = [[0, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 0]]
    assert graph_is_3colorable(g2)

    g3 = [[0, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 0]]
    assert not graph_is_3colorable(g3)

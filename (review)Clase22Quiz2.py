#
# Please implement the greedy VERTEX COVER approximation algorithm
# from this unit into a function called greedy_vc:
#
# while not all edges are covered
# choose a vertex with the most uncovered edges
# put that vertex into the vertex cover
#
# As always, the input graph will be given to you as an adjacency
# matrix. The output should be a list containing the vertexes in
# the vertex cover, listed in the order that your function added them
#
# See the test for an example

def greedy_vc(input_graph):
    # YOUR CODE HERE
    n = len(input_graph)
    assignment = [None]*n
    cover=[]
    while valid == False:
        candidate_index = 0
        max_uncovered_neigbors = 0
        
        for i in range(n):
            if assignment[i] !=1:
                sum_covereded =0
                
                for j in range(n):
                    if input_graph[i][j] == 1 and assignment[j] !=1:
                        sum_uncovered +=1
                if sum_uncovered    > max(max_uncovered_neigbors):
                    candidate_index = i
                    max_uncovered_neigbors = sum_uncovered
                    
        if max_uncovered_neigbors == 0:
            valid = True
        else:
            cover.append(candidate_index)
            assignment[candidate_index] = 1;
        
    size = 0
    for i in range(n):
        if assignment[i] == 1:
            size +=1
            
                    
    return size,cover


def test():
    graph = [[0, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [1, 0, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    cover = greedy_vc(graph)
    # There are multiple possible right answers
    assert (cover == [0, 4, 2] or
            cover == [0, 4, 3] or
            cover == [4, 0, 2] or
            cover == [4, 0, 3])
            
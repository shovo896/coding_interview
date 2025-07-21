# Python program to find celebrity

# Function to find the celebrity
def celebrity(mat):
    n = len(mat)

    # indegree and outdegree array
    indegree = [0] * n
    outdegree = [0] * n

    # query for all edges
    for i in range(n):
        for j in range(n):
            x = mat[i][j]

            # set the degrees
            outdegree[i] += x
            indegree[j] += x

    # find a person with indegree n-1
    # and out degree 0
    for i in range(n):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            return i

    return -1

if __name__ == "__main__":
    mat = [[0, 1, 0],
           [0, 0, 0],
           [0, 1, 0]]
    print(celebrity(mat))

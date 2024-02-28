def transpose(m):
    """
    Computes the transpose of a two-dimensional matrix.

    Parameters:
    m (list of lists): Two-dimensional matrix represented as a list of lists.

    Returns:
    list of lists: Transpose of the input matrix.
    """
    return [list(row) for row in zip(*m)]

print(transpose([[1,2,3],[4,5,6]]))


print(transpose([[1],[2],[3]]))


print(transpose([[3]]))

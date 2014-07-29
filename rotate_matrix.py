def rotate_matrix(matrix):
    """
    display matrix element in a rotate order
    """
    rows = len(matrix)
    columns = len(matrix[0])
    
    return rotate(1, columns, rows, [[0, -1]])
    
def rotate(direction, columns, rows, count):
    
    if rows == 0:
        return count
    
    direction_dict = {1: [0, 1], 
                      2: [1, 0],
                      3: [0, -1],
                      0: [-1, 0]}
    
    
    direction = direction % 4
    
    for col in range(columns):
        
        count.append([count[-1][0] + direction_dict[direction][0],
                      count[-1][1] + direction_dict[direction][1]])
        
    direction += 1
    return rotate(direction, rows - 1, columns, count)

print rotate_matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
    
# output: [[0, -1], [0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [2, 1]]


"""
revise:

def rotate(direction, columns, rows, count):

    if rows == 0:
        return count

    direction_dict = {1: [0, 1],
                      2: [1, 0],
                      3: [0, -1],
                      0: [-1, 0]}

    direction %= 4

    for col in range(columns):

        count.append([count[-1][0] + direction_dict[direction][0],
                      count[-1][1] + direction_dict[direction][1]])

    direction += 1
    return rotate(direction, rows - 1, columns, count)

print rotate_matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]])

# output: [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], 
# [3, 3], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [1, 2], [2, 2], [2, 1]]

"""
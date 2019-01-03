def init_poly(x, x_value, y_value, index):
    return (y_value[index[1]] * (x - x_value[index[0]]) - y_value[index[0]] * (x - x_value[index[1]])) / (x_value[index[1]] - x_value[index[0]])

def poly_at_index(x, x_value, poly_index, index):
    return (poly_index[1] * (x - x_value[index[0]]) - poly_index[0] * (x - x_value[index[1]])) / (x_value[index[1]] - x_value[index[0]])

def nevil(x, x_value, y_value):
    polyindex = {}
    polylen = len(x_value)-1
    for i in range(polylen):
        polyindex[(i, i + 1)] = init_poly(x, x_value, y_value, [i, i + 1])

    count = 1
    while polylen>0:
        j = count + 1
        for i in range(polylen-1):
            polyindex[(i, j)] = poly_at_index(x, x_value, [polyindex[(i,j-1)],polyindex[(i+1,j)]], [i, j])
            j = j + 1
        polylen = polylen-1
        count += 1

    dic = {}
    sum1 = 0
    sum2 = 0
    count = 0

    for i in polyindex:
        if count >= len(x_value) - 1:
            sum1 = abs(polyindex[i] - polyindex[(i[0], i[1] - 1)])
            sum2 = abs(polyindex[i] - polyindex[(i[0] + 1, i[1])])
            dic[i] = min(sum1, sum2)
        count += 1

    index = (0, 2)
    m = dic[index]
    for i in dic:
        if dic[i] < m:
            index = i

    print(polyindex)
    print(dic)
    print(polyindex[index])

if '__main__' == __name__:

    #Example 1:
    '''x = 0.35
    x_value = [2, 1, 0]
    y_value = [-14, -4, 0]
    nevil(x, x_value, y_value)'''

    # Example 2:
    '''x = 1.5
    x_value = [5, 3, -1]
    y_value = [2, 6, 4]
    nevil(x, x_value, y_value)'''

    # Example 3:
    '''x = 1.5
    x_value = [-7, 1, -0.2]
    y_value = [2, 8.8, 0.7]
    nevil(x, x_value, y_value) '''

    # Example 4:
    '''x = 0.5
    x_value = [0, 1.5, -5, 2]
    y_value = [2, 6, 4, 2]
    nevil(x, x_value, y_value) '''

    # Example 5:
    '''x = 0.5
    x_value = [0, 1.5, -5, 2, 5]
    y_value = [2, 6, 4, 2, 5]
    nevil(x, x_value, y_value)'''

    x = 3
    x_value = [1, 2, 4]
    y_value = [1, 0, 1.5]
    nevil(x, x_value, y_value)

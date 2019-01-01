def init_poly(x, x_value, y_value, index):
    return (y_value[index[1]] * (x_value[index[0]] - x) - y_value[index[0]] * (x_value[index[1]] - x)) / (x_value[index[0]] - x_value[index[1]])

def poly_at_index(x, x_value, poly_index, index):
    return (poly_index[1] * (x_value[index[0]] - x) - poly_index[0] * (x_value[index[1]] - x)) / (x_value[index[0]] - x_value[index[1]])

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
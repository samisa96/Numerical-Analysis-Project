def linearapprox(points,x):
    if x<points[0][0] or x>points[len(points)-1][0]:
        print("Can't")
        return None
    intervals=[]
    for i in range(len(points)-1):
        intervals.append((points[i][0],points[i+1][0]))
    print(intervals)
    for i in range(len(intervals)):
        if(intervals[i][0]<=x and intervals[i][1]>=x):
            break
    return (points[i+1][1]-points[i][1])*x/(intervals[i][1]-intervals[i][0])+(points[i][1]*intervals[i][1]-points[i+1][1]*intervals[i][0])/(intervals[i][1]-intervals[i][0])


print(linearapprox([(1,1),(2,2),(3,1),(4,1.5),(5,1)],4.8))
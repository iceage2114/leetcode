
def findMinArrowShots(points):

    if not points:
        return 0

    quickSort(points, 0, len(points))

    arrows = 1
    start = points[0][0]
    end = points[0][1]

    print("p", points)

    for i in range(1, len(points)):
        s = points[i][0]
        e = points[i][1]

        if s > end:
            arrows += 1
            end = e
        else:
            end = min(end, e)

    return arrows

    return len(arrows)


def quickSort(array, start, end):
    if start >= end:
        return

    pivotIndex = start
    pivot = array[start][0]

    for i in range(start + 1, end):
        if array[i][0] < pivot:
            pivotIndex += 1
            swap(array, pivotIndex, i)
    swap(array, start, pivotIndex)

    quickSort(array, start, pivotIndex)
    quickSort(array, pivotIndex + 1, end)


def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp


points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))

# https://leetcode.com/problems/the-skyline-problem/

def getSkyline(buildings):
    """
    Divide-and-conquer algorithm to solve skyline problem,
    which is similar with the merge sort algorithm.
    """
    n = len(buildings)

    # The base cases
    if n == 0:
        return []
    if n == 1:
        x1, x2, h = buildings[0]
        return [[x1, h], [x2, 0]]

    # If there is more than one building,
    # recursively divide the input into two subproblems.
    left_skyline = getSkyline(buildings[:n//2])
    right_skyline = getSkyline(buildings[n//2:])

    # Merge the results of subproblem together.
    return mergeSkylines(left_skyline, right_skyline)


def mergeSkylines(left, right):
    left_n, right_n = len(left), len(right)
    pos_l = pos_r = 0
    curr_y = left_y = right_y = 0
    output = []

    def update_output(x, y):
        """
        Update the final output with the new element.
        """
        # if skyline change is not vertical -
        # add the new point
        if not output or output[-1][0] != x:
            output.append([x, y])
        # if skyline change is vertical -
        # update the last point
        else:
            output[-1][1] = y

    def append_skyline(arr, pos, length, y_pos, curr_y):
        """
        Append the rest of the skyline elements with indice (p, n)
        to the final output.
        """
        while pos < length:
            a, b = arr[pos]
            pos += 1
            if b != curr_y:
                update_output(a, b)
                curr_y = b

    # region where both skylines are present
    while pos_l < left_n and pos_r < right_n:
        point_l, point_r = left[pos_l], right[pos_r]
        # pick the smaller x
        if point_l[0] < point_r[0]:
            x, left_y = point_l
            pos_l += 1
        else:
            x, right_y = point_r
            pos_r += 1
        
        # max height (i.e. y) between both skylines
        max_y = max(left_y, right_y)
        # if there is a skyline change
        if max_y != curr_y:
            update_output(x, max_y)
            curr_y = max_y
    
    # there is only left skyline
    append_skyline(left, pos_l, left_n, left_y, curr_y)
    # there is only right skyline
    append_skyline(right, pos_r, right_n, right_y, curr_y)

    return output



buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
skyline = getSkyline(buildings)
print(skyline)
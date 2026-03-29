"""
New Set: Festival Staffing — Understaffed Hours

Interview Question
You are given staff schedules as inclusive start and exclusive end hour ranges [start, end).
You are also given needed[h], the number of staff required for each hour h (0-23). Write
understaffed(staff, needed) that returns a sorted list of hours where available staff
needed.

Inputs / Examples

staff_1 = [[5, 9], [12, 16]]
needed_1 = [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# understaffed(staff_1, needed_1) => [7, 16]

staff_2 = [[0, 10], [10, 20], [20, 24]]
needed_2 = [1]*24
# => []

staff_3 = [[0, 10], [10, 20], [20, 24]]
needed_3 = [2,2] + [1]*20 + [2,2]
# => [0, 1, 22, 23]

staff_4 =
[[1,4],[1,3],[5,15],[7,15],[13,16],[14,23],[15,19],[13,21],[0,6],[6,10]]
needed_4 = [3, 1, 2, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 1, 3, 2, 0, 4, 0, 0, 0, 0, 0, 0]
# => [0, 17]

staff_5 =
[[12,19],[13,23],[3,12],[5,9],[4,11],[7,9],[2,6],[6,11],[7,17],[8,11]]
needed_5 = [0,3,2,1,0,2,4,4,3,1,3,1,0,0,0,4,0,0,0,0,0,0,0,0]
# => [1, 2, 15]

staff_6 =
[[13,22],[16,19],[3,8],[2,4],[19,21],[10,16],[15,18],[3,7],[0,4],[1,9]]
needed_6 = [0,0,3,1,5,0,0,0,0,0,0,0,0,1,0,0,2,3,0,0,0,0,1,2]
# => [4, 22, 23]
"""

staff_1 = [[5, 9], [12, 16]]
needed_1 = [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
staff_2 = [[0, 10], [10, 20], [20, 24]]
needed_2 = [1] * 24
staff_3 = [[0, 10], [10, 20], [20, 24]]
needed_3 = [2, 2] + [1] * 20 + [2, 2]


staff_4 = [
    [1, 4],
    [1, 3],
    [5, 15],
    [7, 15],
    [13, 16],
    [14, 23],
    [15, 19],
    [13, 21],
    [0, 6],
    [6, 10],
]
needed_4 = [3, 1, 2, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 1, 3, 2, 0, 4, 0, 0, 0, 0, 0, 0]


staff_5 = [
    [12, 19],
    [13, 23],
    [3, 12],
    [5, 9],
    [4, 11],
    [7, 9],
    [2, 6],
    [6, 11],
    [7, 17],
    [8, 11],
]
needed_5 = [0, 3, 2, 1, 0, 2, 4, 4, 3, 1, 3, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0]
# => [1, 2, 15]


staff_6 = [
    [13, 22],
    [16, 19],
    [3, 8],
    [2, 4],
    [19, 21],
    [10, 16],
    [15, 18],
    [3, 7],
    [0, 4],
    [1, 9],
]
needed_6 = [0, 0, 3, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 3, 0, 0, 0, 0, 1, 2]
# => [4, 22, 23]


def understaffed(staff, needed):
    # Step 1 count available staff per hour
    available = [0] * 24
    print(len(needed_1))

    for start, end in staff:
        for hour in range(start, end):
            available[hour] += 1
        
    # step 2 find understaffed hours
    result = []

    for hour in range(24):
        if available[hour] < needed[hour]:
            result.append(hour)

    return result


print(understaffed(staff_1, needed_1))

# Most requested resource in Any 5 - Minute Window
"""
# Most Requested Resource in Any 5-Minute Window

## Problem Statement

You are given an unsorted log of accesses to web resources. Each log entry has three fields:
(access_time_in_seconds, user_id, resource_id). All times are within the same day and are
given as seconds since 00:00:00.

Write a function that returns a tuple (resource_id, count) where count is the maximum
number of accesses to that resource within any 5-minute window (300 seconds), using an
inclusive window: if t_right - t_left ≤ 300, both endpoints count. If the input is empty, return
(None, 0).

## Examples / Test Cases

logs1 = [
    ["200", "user_1", "resource_5"],
    ["3", "user_1", "resource_1"],
    ["620", "user_1", "resource_1"],
    ["620", "user_3", "resource_1"],
    ["34", "user_6", "resource_2"],
    ["95", "user_9", "resource_1"],
    ["416", "user_6", "resource_1"],
    ["58523", "user_3", "resource_1"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["100", "user_3", "resource_6"],
    ["400", "user_6", "resource_2"],
]

logs2 = [
    ["357", "user", "resource_2"],
    ["1262", "user", "resource_1"],
    ["1462", "user", "resource_2"],
    ["1060", "user", "resource_1"],
    ["756", "user", "resource_3"],
    ["1090", "user", "resource_3"],
]

logs3 = [
    ["300", "user_10", "resource_5"],
]

logs4 = [
    ["1", "user_96", "resource_5"],
    ["1", "user_10", "resource_5"],
    ["301", "user_11", "resource_5"],
    ["301", "user_12", "resource_5"],
    ["603", "user_12", "resource_5"],
    ["1603", "user_12", "resource_7"],
]

logs5 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

## Expected Outputs:

most_requested_resource(logs1) => ('resource_1', 3)  # times: 416, 620, 620
most_requested_resource(logs2) => ('resource_1', 2)  # times: 1060, 1262
most_requested_resource(logs3) => ('resource_5', 1)  # times: 300
most_requested_resource(logs4) => ('resource_5', 4)  # times: 1, 1, 301, 301
most_requested_resource(logs5) => ('resource_3', 4)  # times: 1199, 1200, 1201, 1202

## Notes and Constraints

- 5-minute window = 300 seconds, inclusive (t_right - t_left ≤ 300).
- Multiple hits at the same second must all be counted.
- If there are ties across resources for the same maximum count, you may return any one of
  them; tie-breaking can be adjusted if needed.
- Time complexity target: O(N log N) due to sorting per resource; memory: O(N).

## Solution Approach (Sort + Sliding Window)

1) Group access times by resource_id.
2) Sort times for each resource.
3) Use two pointers (left/right) to maintain the largest window with times[right] -
   times[left] ≤ 300.
4) Track the best (resource, count) across resources.

## Python Solution

from collections import defaultdict
from typing import List, Tuple

def most_requested_resource(logs: List[List[str]]) -> Tuple[str, int]:
    # Return (resource_id, max_hits) where max_hits is the highest number of
    # accesses to that resource in any inclusive 300-second window.
    # Returns (None, 0) for empty input.


    times_by_resource = defaultdict(list)
    for t_str, user_id, resource_id in logs:
        times_by_resource[resource_id].append(int(t_str))

    best_resource = None
    best_count = 0

    for resource_id, times in times_by_resource.items():
        times.sort()
        left = 0
        for right in range(len(times)):
            while times[right] - times[left] > 300:
                left += 1
            window_count = right - left + 1
            if window_count > best_count:
                best_count = window_count
                best_resource = resource_id

    if best_resource is None:
        return (None, 0)

    return (best_resource, best_count)

"""
logs1 = [
    ["200", "user_1", "resource_5"],
    ["3", "user_1", "resource_1"],
    ["620", "user_1", "resource_1"],
    ["620", "user_3", "resource_1"],
    ["34", "user_6", "resource_2"],
    ["95", "user_9", "resource_1"],
    ["416", "user_6", "resource_1"],
    ["58523", "user_3", "resource_1"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["100", "user_3", "resource_6"],
    ["400", "user_6", "resource_2"],
]

logs2 = [
    ["357", "user", "resource_2"],
    ["1262", "user", "resource_1"],
    ["1462", "user", "resource_2"],
    ["1060", "user", "resource_1"],
    ["756", "user", "resource_3"],
    ["1090", "user", "resource_3"],
]

logs3 = [
    ["300", "user_10", "resource_5"],
]

logs4 = [
    ["1", "user_96", "resource_5"],
    ["1", "user_10", "resource_5"],
    ["301", "user_11", "resource_5"],
    ["301", "user_12", "resource_5"],
    ["603", "user_12", "resource_5"],
    ["1603", "user_12", "resource_7"],
]

logs5 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

from collections import defaultdict
from typing import List , Tuple

def most_requested_resource(logs:List[List[str]]) -> Tuple[str,int]:

    times_by_resource = defaultdict(list)
    # print(times_by_resource)

    for t_str,user_id,resource_id in logs:
        times_by_resource[resource_id].append(int(t_str))

    best_resource = None
    best_count = 0
    print(times_by_resource.items())
    for resource_id , times in times_by_resource.items():
        times.sort()
        left = 0

        for right in range(len(times)):
            while times[right] - times[left] > 300:
                left += 1
            window_count = right - left + 1
            if window_count > best_count:
                best_count = window_count
                best_resource = resource_id
        
    if best_resource is None:
            return (None,0)
        
    return (best_resource, best_count)

print(most_requested_resource(logs1))
# print(most_requested_resource(logs2))
# print(most_requested_resource(logs3))
# print(most_requested_resource(logs4))
# print(most_requested_resource(logs5))
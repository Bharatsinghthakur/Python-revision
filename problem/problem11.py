"""
You are given an unsorted list of web access logs, where each log entry contains three pieces of information: the access time, the user ID, and the resource ID. The access time is represented as an integer indicating the number of seconds since 00:00:00 (start of the day). Each log entry is in the format [access_time, user_id, resource_id].

Your task is to write a function that identifies all users who have accessed the same resource at least three times within any five-minute window (300 seconds). The logs are not sorted, so your solution should handle them accordingly.

A user satisfies the condition if they access the same resource three or more times such that the difference between the earliest and latest access in that group is less than or equal to 300 seconds.

You must return a list of all such user IDs sorted in alphabetical order. If no user meets the criteria, return an empty list.

Example:

Input:
logs = [
[10, "user_A", "resource_1"],
[100, "user_A", "resource_1"],
[250, "user_A", "resource_1"],
[400, "user_B", "resource_2"],
[450, "user_B", "resource_2"],
[800, "user_B", "resource_2"]
]

Output:
["user_A"]
"""

"""  
from collections import defaultdict
from typing import List, Tuple


def users_with_three_accesses_in_5min(logs: List[List]) -> List[str]:
   
   # Returns sorted list of user IDs who accessed the same resource
    #at least 3 times within any 5-minute (<=300s) window.
    

    # 1) Group timestamps by (user, resource)
    times_by_user_resource = defaultdict(list)
    for t, user, resource in logs:
        times_by_user_resource[(user, resource)].append(int(t))

    # 2) For each (user, resource), sort timestamps and check via sliding window
    flagged_users = set()

    for (user, resource), times in times_by_user_resource.items():
        times.sort()

        # Sliding window: expand 'r', shrink 'l' to keep window within 300s
        l = 0
        for r in range(len(times)):

            # Ensure the window satisfies times[r] - times[l] <= 300
            while times[r] - times[l] > 300:
                l += 1

            # Check count in window
            if r - l + 1 >= 3:
                flagged_users.add(user)
                break  # No need to check further for this user-resource

    # 3) Return alphabetically sorted list of unique user IDs
    return sorted(flagged_users)
"""

# Logs  

logs = [
    [10, "user_A", "resource_1"],
    [100, "user_A", "resource_1"],
    [250, "user_A", "resource_1"],
    [400, "user_B", "resource_2"],
    [450, "user_B", "resource_2"],
    [800, "user_B", "resource_2"],
]
from collections import defaultdict


def solution(logs):
    # group by (user,resource)

    times_by_user_resource = defaultdict(list)

    for t, user, resource in logs:
        times_by_user_resource[(user, resource)].append(t)

    # sliding window for each pair

    flagged_user = set()

    for (user, resource), times in times_by_user_resource.items():
        times.sort()
        l = 0
        for r in range(len(times)):
            while times[r] - times[l] > 300:
                l += 1
            if r - l + 1 >= 3:
                flagged_user.add(user)
                break

    # returned sorted alpahbateical order
    return sorted(flagged_user)

print(solution(logs))
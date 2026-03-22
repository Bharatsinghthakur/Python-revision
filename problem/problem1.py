
'''
Implement grouping(events, N) where:

events is a list of ["CONNECT" / "DISCONNECT", personA, personB]
Graph is undirected, CONNECT is idempotent, DISCONNECT is a no-op if absent
N is 1, 2, 3 etc.

Return:

ge: sorted list of people with degree >= N
lt: sorted list of people with degree < N
events = [
    ["CONNECT", "Alice", "Bob"],
    ["CONNECT", "Clara", "Bob"],
    ["CONNECT", "Alice", "Clara"],
    ["CONNECT", "Dave", "Eve"],
    ["CONNECT", "Eve", "Frank"],
    ["CONNECT", "Frank", "Dave"],
    ["DISCONNECT", "Alice", "Bob"],
    ["CONNECT", "Alice", "Frank"],
    ["CONNECT", "Bob", "Dave"],
    ["DISCONNECT", "Dave", "Eve"],
    ["CONNECT", "Clara", "Eve"],
    ["CONNECT", "Bob", "Eve"],
    ["CONNECT", "Alice", "Eve"],
    ["CONNECT", "Bob", "Clara"],
    ["DISCONNECT", "Frank", "Dave"],
    ["DISCONNECT", "Clara", "Bob"],
    ["CONNECT", "Frank", "Clara"]
]
'''

# def grouping(events, N):
#     edges = set()
#     people = set()

#     for action, u, v in events:
#         # step 1: track people
#         # step 2: normalize edge
#         # step 3: add/remove edge

#     # step 4: initialize degree
#     # step 5: count degrees
#     # step 6: split results

#     return ge, lt

events = [
    ["CONNECT", "Alice", "Bob"],
    ["CONNECT", "Clara", "Bob"],
    ["CONNECT", "Alice", "Clara"],
    ["CONNECT", "Dave", "Eve"],
    ["CONNECT", "Eve", "Frank"],
    ["CONNECT", "Frank", "Dave"],
    ["DISCONNECT", "Alice", "Bob"],
    ["CONNECT", "Alice", "Frank"],
    ["CONNECT", "Bob", "Dave"],
    ["DISCONNECT", "Dave", "Eve"],
    ["CONNECT", "Clara", "Eve"],
    ["CONNECT", "Bob", "Eve"],
    ["CONNECT", "Alice", "Eve"],
    ["CONNECT", "Bob", "Clara"],
    ["DISCONNECT", "Frank", "Dave"],
    ["DISCONNECT", "Clara", "Bob"],
    ["CONNECT", "Frank", "Clara"]
]

# def grouping(events,N):
    # active_edges = set()
    # people = set()

    # for action,u,v in events:
    #     people.add(u)
    #     people.add(v)

    #     if u == v:
    #         continue

    #     a,b = (u,v) if u < v else (v,u)

    #     if action == 'connect':
    #         active_edges.add((a,b))
    #     elif action == 'disconnect':
    #         active_edges.discard((a,b))
    
    # degree = {p:0 for p in people}

    # for a,b in active_edges:
    #         degree[a] += 1
    #         degree[b] += 1
        
    # ge = sorted([p for p,d, in degree.items() if d >= N])
    # lt = sorted([p for p,d in degree.items() if d < N])

    # return ge,lt

# from collections import defaultdict

# def grouping(events, N):
#     active_edges = set()
#     people = set()

#     for action, u, v in events:
#         people.add(u)
#         people.add(v)

#         if u == v:
#             continue

#         a, b = (u, v) if u < v else (v, u)

#         if action == "CONNECT":
#             active_edges.add((a, b))
#         elif action == "DISCONNECT":
#             active_edges.discard((a, b))

#     degree = {p: 0 for p in people}

#     for a, b in active_edges:
#         degree[a] += 1
#         degree[b] += 1

#     ge = sorted([p for p, d in degree.items() if d >= N])
#     lt = sorted([p for p, d in degree.items() if d < N])

#     return ge, lt
# print(grouping(events,1))
# print(grouping(events,2))
# print(grouping(events,3))

def grouping(events, N):
    degree = {}
    edges = set()

    for action, u, v in events:
        # track people
        if u not in degree:
            degree[u] = 0
        if v not in degree:
            degree[v] = 0

        if u == v:
            continue

        a, b = sorted([u, v])

        if action == "CONNECT":
            if (a, b) not in edges:
                edges.add((a, b))
                degree[a] += 1
                degree[b] += 1

        elif action == "DISCONNECT":
            if (a, b) in edges:
                edges.remove((a, b))
                degree[a] -= 1
                degree[b] -= 1

    ge = sorted([p for p in degree if degree[p] >= N])
    lt = sorted([p for p in degree if degree[p] < N])

    return ge, lt

print(grouping(events,1))
print(grouping(events,2))
print(grouping(events,3))
from collections import defaultdict
from itertools import combinations

edges = set()
vertices = set()
graph = defaultdict(set)

for line in open("input.txt"):
    a, b = line.strip().split("-")
    edges.add((a, b))
    edges.add((b, a))
    vertices.add(a)
    vertices.add(b)

    graph[a].add(b)
    graph[b].add(a)


def part1():
    ans1 = 0
    for v1, v2, v3 in combinations(vertices, 3):
        if any([a.startswith("t") for a in [v1, v2, v3]]):
            if (v1, v2) in edges and (v2, v3) in edges and (v1, v3) in edges:
                ans1 += 1

    print("Part1: ", ans1)


# BFS in Adjacency List
def part2():
    all_components = []

    for v in graph:
        visited = set()
        component = set()
        if v not in visited:
            q = [v]
            while q:
                node = q.pop(0)
                if node not in visited:
                    visited.add(node)
                    if all([(node, v2) in edges for v2 in component]):
                        component.add(node)
                        for adj in graph[node]:
                            q.append(adj)
            if component not in all_components:
                all_components.append(component)

    print("Part2: ", ",".join(sorted(max(all_components, key=lambda x: len(x)))))


part1()
part2()

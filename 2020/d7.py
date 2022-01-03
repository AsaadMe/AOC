import re

def traverse_graph(graph, node1, visited):
    if node1 == 'shiny gold':
        return 1
    
    neighs = graph[node1]
    if neighs:
        for node2 in neighs:
            node2 = node2[1]
            if node2 not in visited:
                visited.append(node2)
                if a := traverse_graph(graph, node2, visited):
                    return a
                
def build_graph():
    with open('2020/input','r') as file:
        input = file.readlines()
    
    graph = {}   
    for rule in input:
        rule = rule.strip()
        lname = re.match(r'^(\w* \w*) bags', rule).group(1)
        if 'no other' in rule:
            graph[lname] = None
        else:
            neighnors = re.findall(f'(\d*) (\w* \w*) bag', rule)
            graph[lname] = neighnors
            
    return graph


def part1():
    g = build_graph()
    ans = 0
    for n in g:
        if n != 'shiny gold' and traverse_graph(g, n, [n]):
            ans += 1
    return ans
    
def part2():
    g = build_graph()
    
    def step(node1):
        ans = 0
        neighs = g[node1]
        if neighs:
            for neigh in neighs:
                ans += int(neigh[0])*step(neigh[1]) + int(neigh[0])
        else:
            ans = 0
        return ans
    
    return step('shiny gold')

print(part1())
print(part2())
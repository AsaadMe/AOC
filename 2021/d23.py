from copy import deepcopy
import functools

board = (None, None, ('B','D','D','C'), None, ('A','C','B','D'), None, ('B','B','A','D'), None, ('C','A','C','A'), None, None)
rooms_ready_to_get = (False,)*11
room_id = {2:"A", 4:"B", 6:"C", 8:"D", "A":2, "B":4, "C":6, "D":8}
pod_costs = {"A":1, "B":10, "C":100, "D":1000}

def get_valid_range(board, i):
    leftmost_obsticle = -1
    rightmost_obsticle = 11
    
    for j in range(i+1, len(board)):
        if (board[j] is not None) and (not isinstance(board[j], list)):
            rightmost_obsticle = j
            break
    
    for j in range(i-1, -1, -1):
        if (board[j] is not None) and (not isinstance(board[j], list)):        
            leftmost_obsticle = j
            break
            
    return (leftmost_obsticle, rightmost_obsticle)



@functools.cache
def step(board, rooms_ready_to_get):
    board = [list(a) if isinstance(a,tuple) else a for a in board]
    rooms_ready_to_get = list(rooms_ready_to_get)
    if board == [None, None, ['A']*4, None, ['B']*4, None, ['C']*4, None, ['D']*4, None, None]:
        return 0
     
    min_ans = float('inf')
    for i, obj in enumerate(board):
        if isinstance(obj, list):
            if obj and not all([a==room_id[i] for a in obj]):
                next_board = deepcopy(board)
                next_rooms_ready = rooms_ready_to_get.copy()
                lobs, robs = get_valid_range(board ,i)
                
                pod = obj[0]
                rid = room_id[pod]
                if rooms_ready_to_get[rid] and (lobs < rid < robs) and (rid != i): # directly from a list to the correct room
                    next_board[rid].insert(0, pod)
                    cost = ((4-len(obj)) + abs(i-rid) + 1 + (4-len(board[rid])))*pod_costs[pod]
                    next_board[i].pop(0)
                    if len(obj) == 0 or all([a==room_id[i] for a in next_board[i]]):
                        next_rooms_ready[i] = True 
                    next_board = tuple([tuple(a) if isinstance(a, list) else a for a in next_board])
                    next_rooms_ready = tuple(next_rooms_ready)
                    cost += step(next_board, next_rooms_ready)
                    if cost < min_ans:
                        print(next_board)
                        min_ans = cost
                    
                else: # from list to hall
                    if robs - lobs != 1:
                        for j in range(lobs+1, robs):
                            next_board = deepcopy(board)
                            next_rooms_ready = rooms_ready_to_get.copy()
                            if board[j] == None:
                                next_board[j] = pod
                                cost = ((4-len(obj)) + abs(i-j)+1)*pod_costs[pod]
                                next_board[i].pop(0)
                                if len(obj) == 0 or all([a==room_id[i] for a in next_board[i]]):
                                    next_rooms_ready[i] = True
                                next_board = tuple([tuple(a) if isinstance(a, list) else a for a in next_board])
                                next_rooms_ready = tuple(next_rooms_ready)
                                cost += step(next_board, next_rooms_ready)
                                if cost < min_ans:
                                    print(next_board)
                                    min_ans = cost
                                  
        elif isinstance(obj, str): # from hall to correct room
            next_board = deepcopy(board)
            next_rooms_ready = rooms_ready_to_get.copy()
            lobs, robs = get_valid_range(board ,i)
            pod = obj
            rid = room_id[pod]
            if rooms_ready_to_get[rid] and (lobs < rid < robs):
                next_board[rid].insert(0, pod)
                next_board[i] = None
                cost = (4-len(board[rid])+abs(i-rid))*pod_costs[pod]
                next_board = tuple([tuple(a) if isinstance(a, list) else a for a in next_board])
                next_rooms_ready = tuple(next_rooms_ready)
                cost += step(next_board, next_rooms_ready) 
                if cost < min_ans:
                    print(next_board)
                    min_ans = cost     
    return min_ans               
            
            

a = step(board, rooms_ready_to_get)
print(a)
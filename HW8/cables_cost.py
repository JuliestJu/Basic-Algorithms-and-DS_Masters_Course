import heapq

def min_cost_to_connect_cables(cables):
    # Create a min-heap from the list of cables
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Extract the two smallest lengths
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Cost to connect these two cables
        cost = first + second
        
        # Add the combined cable length back to the heap
        heapq.heappush(cables, cost)
        
        # Add the cost to the total cost
        total_cost += cost
    
    return total_cost

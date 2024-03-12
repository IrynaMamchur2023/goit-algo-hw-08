import heapq

def min_cost_of_network_cables(cable_lengths):
    n = len(cable_lengths)
    result = []

    heap = [(length, index) for index, length in enumerate(cable_lengths)]
    heapq.heapify(heap)

    while len(heap) > 1:
        
        shortest1, index1 = heapq.heappop(heap)
        shortest2, index2 = heapq.heappop(heap)
        
        combined_length = shortest1 + shortest2
        result.append((index1, index2))
        
        heapq.heappush(heap, (combined_length, n))
        n += 1

    return result


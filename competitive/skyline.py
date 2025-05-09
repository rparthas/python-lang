import heapq

def getSkyline(buildings):
    # Create events for all building points
    events = []
    for left, right, height in buildings:
        # Entering event
        events.append((left, -height, right))  # Negative height for entering
        # Exiting event
        events.append((right, 0, 0))  # Height 0 for exiting

    # Sort events by x-coordinate
    events.sort()

    # Initialize result and max heap
    result = []
    heap = [(0, float('inf'))]  # (height, ending_x)

    for pos, neg_h, ending in events:
        # Remove buildings that have ended
        print("Current state:", heap)
        print("Adding event:", pos, neg_h, ending)
        while heap and heap[0][1] <= pos:
            heapq.heappop(heap)

        # Add new building
        if neg_h != 0:
            heapq.heappush(heap, (neg_h, ending))

        # If the max height changes, add to the result
        if not result or result[-1][1] != -heap[0][0]:
            result.append([pos, -heap[0][0]])

    return result

if __name__ == "__main__":
    buildings = [[1,5,11], [2,7,6], [3,9,13], [12,16,7], [14,25,3], [19,22,18]]
    print(getSkyline(buildings))

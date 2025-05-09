import heapq

def carPooling(trips,capacity):
    # return carPoolingPrefix(trips,capacity)
    return carPoolingHeap(trips,capacity)


def carPoolingPrefix(trips,capacity):
    # timeline will record net passengers picked/dropped at each km mark
    timeline = [0] * 1001  # Because max distance is up to 1000

    # Mark the start and end of each trip
    for num_passengers, start, end in trips:
        timeline[start] += num_passengers
        timeline[end] -= num_passengers

    # Traverse the timeline, tracking the current number of passengers
    current_passengers = 0
    for passengers in timeline:
        current_passengers += passengers
        if current_passengers > capacity:
            return False

    return True



def carPoolingHeap(trips, capacity):
    # Sort trips by start time
    trips.sort(key=lambda x: x[1])
    # Min-heap to track active trips by drop-off time
    heap = []
    current_passengers = 0

    for num_passengers, start, end in trips:
        # Drop off passengers for trips that have ended
        while heap and heap[0][0] <= start:
            drop_off_time, passengers = heapq.heappop(heap)
            current_passengers -= passengers

        # Pick up new passengers
        current_passengers += num_passengers
        if current_passengers > capacity:
            return False

        heapq.heappush(heap, (end, num_passengers))

    return True


if __name__ == "__main__":
    # Example 1 – Overlapping trips exceed capacity
    assert carPooling([[2, 1, 5], [3, 3, 7]], 4) == False

    # Example 2 – Overlapping trips within capacity
    assert carPooling([[2, 1, 5], [3, 3, 7]], 5) == True

    # Edge Case – One trip
    assert carPooling([[1, 0, 1000]], 1) == True

    # Edge Case – Multiple non-overlapping trips
    assert carPooling([[2, 1, 3], [3, 3, 5], [1, 5, 7]], 3) == True

    # All passengers at same start, exceed capacity
    assert carPooling([[4, 2, 10], [2, 2, 9], [1, 2, 5]], 6) == False

    # Trip ends where another begins
    assert carPooling([[2, 1, 5], [3, 5, 7]], 3) == True

    # Empty trips list
    assert carPooling([], 10) == True

    # Zero capacity
    assert carPooling([[1, 0, 2]], 0) == False

    # Passenger drop-off before next pick-up
    assert carPooling([[3, 2, 4], [2, 4, 6], [1, 6, 8]], 3) == True

    # Extreme capacity pressure at a single location
    assert carPooling([[2, 1, 10], [3, 2, 3], [2, 2, 5]], 5) == False

    # Multiple overlapping within window
    assert carPooling([[1, 1, 3], [2, 2, 4], [1, 3, 5], [1, 4, 6]], 3) == True

    print("All test cases passed! 🚗💨")

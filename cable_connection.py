import heapq

def min_connection_cost(cable_lengths):
    """
    Calculate the minimum total cost to connect network cables.
    
    Args:
        cable_lengths (list): List of cable lengths
        
    Returns:
        int: Minimum total connection cost
    """
    # Convert the list to a heap
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    steps = []
    
    # Connect cables until only one is left
    while len(cable_lengths) > 1:
        # Get the two shortest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Calculate connection cost
        connection_cost = first + second
        
        # Add to total cost
        total_cost += connection_cost
        
        # Track this step
        steps.append((first, second, connection_cost))
        
        # Add the new cable back to the heap
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost, steps

if __name__ == "__main__":
    cable_lengths = [4, 2, 7, 6, 9]
    print(f"Example cable lengths: {cable_lengths}")
    
    cost, steps = min_connection_cost(cable_lengths.copy())
    print(f"Minimum connection cost: {cost}")
   
    print("\nDetailed execution:")
    
    total = 0
    for i, (first, second, connection) in enumerate(steps, 1):
        total += connection
        print(f"Step {i}: Connected {first} + {second} = {connection}, Current total cost: {total}")
    
    print(f"\nFinal result: Minimum connection cost = {cost}")

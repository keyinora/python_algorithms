def verify_tsp(paths, dist, actual_path):
    total_distance = 0
    # Sum the distances between each consecutive city in the actual path
    for i in range(len(actual_path) - 1):
        total_distance += paths[actual_path[i]][actual_path[i + 1]]
    
    # Check if the total distance is less than the specified distance
    return total_distance < dist

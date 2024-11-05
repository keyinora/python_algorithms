def tsp(cities, paths, dist):
    routes = permutations(cities)  # Get all possible routes
    # Iterate over each possible route
    for route in routes:
        total_distance = 0
        # Calculate the total distance for the current route
        for i in range(len(route) - 1):
            total_distance += paths[route[i]][route[i + 1]]
        # Check if the distance of this route is less than the threshold
        if total_distance < dist:
            return True
    # If no route is shorter than the specified distance, return False
    return False

# Don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

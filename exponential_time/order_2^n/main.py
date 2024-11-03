def power_set(input_list):
    # Check if the input list is empty
    if not input_list:
        return [[]]  # Base case: power set of an empty list is a list containing an empty list

    # Initialize an empty list to hold all subsets
    final_subsets = []
    # Recursive step: get the power set of the list excluding the first element
    # Iterate over each subset from the recursive call
    for subset in power_set(input_list[1:]):        
        # Add the subset itself
        final_subsets.append(subset)
        # Add a new subset that includes the first element of the input list
        final_subsets.append([input_list[0]] + subset)        
    return final_subsets

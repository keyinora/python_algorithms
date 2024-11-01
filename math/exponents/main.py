def get_estimated_spread(audiences_followers):
    # Return 0 if the list is empty
    if not audiences_followers:
        return 0
    # Calculate the average number of followers each follower has
    total_followers = sum(audiences_followers)
    average_audience_followers = total_followers / len(audiences_followers)
    
    # Calculate the number of followers (the author's followers)
    num_followers = len(audiences_followers)
    
    # Apply the spread formula
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    return estimated_spread

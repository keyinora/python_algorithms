def get_follower_prediction(follower_count, influencer_type, num_months):
    n = 0
    match(influencer_type):
        case 'fitness':
            n = 4
        case 'cosmetic':
            n = 3
        case _:
            n = 2
    return follower_count * (n ** num_months)

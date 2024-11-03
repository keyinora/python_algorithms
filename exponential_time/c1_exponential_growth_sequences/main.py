def exponential_growth(n, factor, days):
    growth_sequence = [n]
    for i in range(days):
        growth_sequence.append(growth_sequence[-1] * factor)
    return growth_sequence

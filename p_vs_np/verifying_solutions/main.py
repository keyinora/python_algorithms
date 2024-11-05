def get_num_guesses(length):
    total_guesses = 0
    # Sum all possible passwords for lengths from 1 to the given length
    for n in range(1, length + 1):
        total_guesses += 26 ** n
    return total_guesses

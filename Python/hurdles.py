

# Hackerrank solution, how many times do we need to collect a powerup such that all hurdles can be cleared.
def hurdle(k, height):
    highest_delta = 0
    for h in height:
        if h - k > highest_delta:
            highest_delta = h - k
    
    return highest_delta
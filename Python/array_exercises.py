def smallest_non_occuring_positive_integer(A):
    sorted_array = sorted(A)
    last_positive = 0
    for n in sorted_array:
        if n < 0:
            pass
        if n >= 0:
            if n-last_positive > 1:
                return last_positive + 1
            else:
                last_positive = n
    
    if last_positive == sorted_array[-1]:
        return last_positive + 1
    
    return 1
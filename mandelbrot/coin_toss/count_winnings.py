def count(n, ct_series):
    """Naive solution for summing the cumulative winnings for heads per coin toss."""
    
    winnings_h = []
    total = 0

    for i in ct_series:
        if i > 0:
            total += 1
            winnings_h.append(total)
        else:
            total -= 1
            winnings_h.append(total)
    
    return winnings_h

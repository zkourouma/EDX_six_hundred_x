def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24      equals n
    Otherwise returns False.
    """
    if n == 0:
        return False
    elif n%5 == 0 or n%8 == 0 or n%24 == 0:
        return True
    for a in range(1,n):
        for b in range(1,n):
            for c in range(n):
                if n%((a*5) + (b*8) + (c*24)) == 0:
                    return True
    return False
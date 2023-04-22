def powAB(a, b):
    if b == 1: return a
    if b == 0: return 1
    if b < 0: return 1 / (a * powAB(a, -b - 1))
    else: return a * powAB(a, b - 1)
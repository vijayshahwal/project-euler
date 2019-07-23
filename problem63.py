ns = 0
    # Two-digit `i` will always give len(i**n) > n
for i in range(1, 10):
            for p in range(1, 22):
                        n = len(str(i ** p))
                        if n == p:
                                    ns += 1
                        elif n < p:
                                    break
print(ns)

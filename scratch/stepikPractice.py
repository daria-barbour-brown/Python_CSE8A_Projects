def is_positive_or_multiple_of_7(n):
    while n > 0:
        if n % 7 == 0:
            break
        n = n -3
    return n

print(is_positive_or_multiple_of_7(100))
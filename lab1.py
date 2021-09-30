#calculator.py

def sum(m,n):
    if n > 0:
        for i in range(n):
            m  = m + 1
    else:
        for i in range(-n):
            m  = m - 1
    return m

def divide(m,n):
    i = 0

    if n == 0:
        print("Error: You have set the divider to 0!")
        return

    #in this case m is zero so te result is zero
    if m == 0:
        return i

    #m and n have the same sign, so the result is positive
    if m*n > 0:
        while m*n > 0:
            m = m - n
            if m*n >= 0:
                i = i + 1
        return i

    #m and n don't have the same sign, so the result is negative
    else: 
        while m*n < 0:
            m = m + n
            if m*n <= 0:
                i = i + 1
        return -i

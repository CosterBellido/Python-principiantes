# Convertidor de numeros romanos a decimal
tallies = {'I': 1,
           'V': 5,
           'X': 10,
           'l': 50,
           'C': 100,
           'D': 500,
           'M': 1000
           }
def romano_decimal(nan_romano):
    sum = 0
    for i in range(len(nan_romano) - 1):
        left = nan_romano [i]
        right = nan_romano [i + 1]
        if tallies [left] < tallies [right]:
            sum -= tallies [left]
        else:
            sum += tallies[left]
    sum += tallies[nan_romano[-1]]
    return sum
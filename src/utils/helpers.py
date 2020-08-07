import math


def tooman2euro(tooman):
    one_euro_in_tooman = 25000
    return tooman/one_euro_in_tooman


def preack_even_point(income, cost):
    for month in range(len(cost)):
        #print( income[month],cost[month])
        if (income[month] - cost[month]) > 0:
            return month, income[month]
    return 0, 0


def millify(n, curency="Euros"):
    millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
    n = float(n)
    millidx = max(
        0,
        min(len(millnames)-1,
            int(math.floor(0 if n == 0 else math.log10(abs(n))/3)))
    )

    return '{:.0f}{} {}'.format(n / 10**(3 * millidx), millnames[millidx], curency)

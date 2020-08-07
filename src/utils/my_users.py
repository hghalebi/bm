import math


def expoential_growth(x, maximum=1000, half_life=0.5, scalibilty=2):
    """
    generate data based on f(x)= 1/(1+exp(x))
    """

    return maximum/(half_life+math.exp(-x/scalibilty))


def user_projection(f=expoential_growth, months=12, maximum=1000, half_life=0.5, scalibilty=2):
    """
    This fonction generate hypotical number of uesers
    f: fonction which based on it we call calculate the numbers
    Months: Distrubution of users is based months number
    it returns list of potential users
    """

    return [int(f(x, maximum=maximum, half_life=half_life, scalibilty=scalibilty)) for x in range(int(-months/2), int(months/2))]

import math

while True:
    try:
        p = float(input("\nProbability of better team winning: "))

        if 0.5 > p or p > 1:
            raise Exception("valueNotInRange")

        g = int(input("\nLowest number of games the better team must win: "))

        if g % 2 == 0:
            raise Exception("valueNotOdd")

        f = g - 1

        terms = []
        result = 0

        for c in range(0, g):
            terms.append(math.comb((f + c), f) * p**g * (1 - p)**(f - f + c))

        for i in terms:
            result += i

        print("\nResult:", result)

    except Exception as e:
        print(e)

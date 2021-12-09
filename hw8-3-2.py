# Author: ATN 12/9/21

def sum_odds(odds):
    numbers = 0
    x = 0
    while x < len(odds):
        if((odds[x] % 2) == 0):
            x += 1
            continue
        else:
            numbers += odds[x]
            x += 1
    return(numbers)

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)

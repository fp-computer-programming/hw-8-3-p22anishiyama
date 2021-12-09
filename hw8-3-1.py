# Author: ATN 12/9/21

def count_odds(odds):
    numbers = 0
    x = 0
    while x < len(odds):
        if((odds[x] % 2) == 0):
            x += 1
            continue
        else:
            x += 1
            numbers += 1
    return(numbers)

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)

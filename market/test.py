sorted_integers = [0, 1, 5, 8, 14, 18, 44, 81, 89, 99, 102]

count = 0

for integer in sorted_integers:
    if 10 < integer < 20:
        count = count + 1
    # print(integer)

print(count)
# Getting numbers less than 5 in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_5 = []
for i in range(len(numbers)):
    if numbers[i] < 5:
        less_than_5.append(numbers[i])

print(less_than_5)
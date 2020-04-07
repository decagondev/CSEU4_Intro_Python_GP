# list comprehensions

# loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubles_if_even = []
for num in lst:
    if num % 2 == 0:
        doubles_if_even.append(num * 2)

dub = [num * 2 for num in lst if num % 2 == 0]

# num = 1
# print(1 % 2)
# num = 2

print(lst)
print(doubles_if_even)
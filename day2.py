# Passing by value Vs passing by Ref

# define a doubling function that passes args by value
def mult2(x):
    return x * 2

# define a doubling function that passes args by reference
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


# # try out the functions
# a = 12

# new_number = mult2(a)
# print(new_number)

# lst = [2, 4, 6, 8] # mutable
# mult2_list(lst)

# for num in lst:
#     print(num)



#===========================================================

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 (1 + 5 + 5 + 8 + 7) // 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# UNDERSTAND

# how many integers to work with? (min 3 ints)
# if there are more than 1 largest or smallest value what do we do? we remove only 1
# do we need to account for floating points in our answers? no we only want to use int answers //

# PLAN & EXECUTE

def centered_avg1(ints):
    pass

def centered_avg2(ints):
    pass

# tests


numbers = [1, 41, 34, 29, 50, 50]

import time

start = time.time()
for i in range(1000):
    centered_avg1(numbers)
end = time.time()

print(end - start)

print("-----------------------")

start = time.time()
for i in range(1000):
    centered_avg2(numbers)
end = time.time()

print(end - start)
# a = 41 + 34 + 29 + 50
# print(a)

# b = a // 4

# print(b)


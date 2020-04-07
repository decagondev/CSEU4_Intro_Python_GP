# pass by value
n = 7 # @4567 => 7

def mult(n):
    n = 12 # @7956
    return n * 2 # @7956

print(n)
print(mult(n))
print(n)





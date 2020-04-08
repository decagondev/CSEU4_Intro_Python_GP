class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = ""
        output += self.name + "\n\n"
        cat_index = 1
        for c in self.categories:
            output += "  " + str(cat_index) + ". " + c + "\n"
            cat_index += 1
        return output

s = Store("Bobs Store", ["Books", "Weapons", "Food"])

print(s)


# l = [12, 23, 34, 56, 78]
# for i,j in enumerate(l):
#     print(i, j)
class Chocolates:
    def __init__(self, weight, price, types, ID):
        self.weight = weight
        self.price = price
        self.types = types
        self.ID = ID

def iterativeChocDist(choc, students):
    distChocs = []
    for c in range(len(students)):
        if c < len(choc):
            distChocs.append((students[c], choc[c]))
        else:
            break
    return distChocs

def recursiveChocDist(choc, students, index=0):
    if index >= len(students) or index >= len(choc):
        return []
    else:
        return [(students[index], choc[index])] + recursiveChocDist(choc, students, index + 1)

#test cases using objects
choc = [
    Chocolates(6, 3, "Dark Chocolate", "001"),
    Chocolates(5, 2, "Almond Chocolate", "002"),
    Chocolates(8, 5, "Milk Chocolate", "003"),
    Chocolates(4, 2, "White Chocolate", "004"),
    Chocolates(7, 4, "Peanut Butter Chocolate", "005"),
    Chocolates(5, 10, "Matcha White Chocolate", "006"),
    Chocolates(4, 8, "Orange Flavored Chocolate", "007"),
    Chocolates(10, 10, "Hazelnut Chocolate", "008"),
    Chocolates(6, 7, "Mint Chocolate", "009"),
    Chocolates(6, 9, "Crunchy Milk Chocolate", "010"),
    ]

students = ["Maryam", "Athbah", "Fatima", "Lateefa", "Mansour", "Khalifa", "Matar", "Mohammed"]

#testing the iterative function using the objects above
iterative_dist = iterativeChocDist(choc, students)
print("Iterative Distribution:")
for student, chocolate in iterative_dist:
    print(f"{student} gets {chocolate.types}")

# Test recursive function
recursive_dist = recursiveChocDist(choc, students)
print("\nRecursive Distribution:")
for student, chocolate in recursive_dist:
    print(f"{student} gets {chocolate.types}")





#TASK 2
def weightSortChoc(choc):
    return sorted(choc, key=lambda x: x.weight)

def priceSortChoc(choc):
    return sorted(choc, key=lambda x: x.price)

# Test cases
weightSort = weightSortChoc(choc)
priceSort = priceSortChoc(choc)

print("\nChocolates sorted by weight:")
for chocolate in weightSort:
    print(f"Type: {chocolate.types}, Weight: {chocolate.weight}")

print("\nChocolates sorted by price:")
for chocolate in priceSort:
    print(f"Type: {chocolate.types}, Price: {chocolate.price}")





#TASK 3
def chocPriceSearch(choc, price):
    for student, chocolate in choc:
        if chocolate.price == price:
            return student
    return None

def chocWeightSearch(choc, weight):
    for student, chocolate in choc:
        if chocolate.weight == weight:
            return student
    return None

# Test cases
price = 5
StudentSpecifiedPrice = chocPriceSearch(iterative_dist, price)
if StudentSpecifiedPrice:
    print(f"\nThe student who is holding a chocolate with price {price} is: {StudentSpecifiedPrice}")
else:
    print(f"No student is found holding a chocolate with price {price}")

weight = 9
StudentSpecifiedWeight = chocWeightSearch(iterative_dist, weight)
if StudentSpecifiedWeight:
    print(f"The student who is holding a chocolate with weight {weight} is: {StudentSpecifiedWeight}")
else:
    print(f"No student is found holding a chocolate with weight {weight}")

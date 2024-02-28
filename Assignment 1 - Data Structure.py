import time # we import the time to later find T(n) and explain the time complexity
import matplotlib.pyplot as plt # we import matplotlib to plot the T(n) graphs easily

class Chocolates:
    '''
    Class to represent the chocolates
    '''
    def __init__(self, weight, price, types, ID): # this function will initialize the attributes
        self.weight = weight
        self.price = price
        self.types = types
        self.ID = ID
timer = 0 # this creates a global variable to keep track of the execution time

def iterativeChocDist(choc, students): # defined the function to distribute the chocolates iteratively to students
    global timer # here we used the global timer variable
    start = time.time() # starts the timer
    distChocs = [] # create an empty list to store distributed chocolates
    for c in range(len(students)): # for loop to iterate over the range of students
        if c < len(choc): # check if there is any chocolate left
            distChocs.append((students[c], choc[c])) # add the chocolate-student pair to the list
        else:
            break # exit loop
    end = time.time() # stops the timer
    timer += end - start # this will update the timer
    print("This algorithm takes", end - start, "seconds for the iterative distribution")
    return distChocs # returns the list of distributed chocolates

def recursiveChocDist(choc, students, index = 0): # now we define another function to distribute chocolates recursively to students
    global timer # here we used the global timer variable
    start = time.time() # starts the timer
    if index >= len(students) or index >= len(choc): # check if the index exceeds the length of students or chocolates
        end = time.time() # stops the timer
        timer += end - start # this will update the timer
        print("This algorithm takes", end - start, "seconds for the recursive distribution")
        return [] # this will return an empty list if the index is out of range
    else:
        result = [(students[index], choc[index])] + recursiveChocDist(choc, students, index + 1) # recursively distribute chocolates
    end = time.time() # stops the timer again
    timer += end - start # this will update the timer
    return result # returns the result of the recursive distribution

# T(n) of iterative distribution
def iterativeDistribution(n):
    # simulate distribution with n students and n chocolates
    students = list(range(n))
    choco = list(range(n))
    return students, choco

# T(n) of recursive distribution
def recursiveDistribution(n):
    # simulate distribution with n students and n chocolates
    students = list(range(n))
    choco = list(range(n))
    return students, choco

# change the input size and measure the time taken for each distribution method
input_size = list(range(1, 1001, 100))
iterative_t = []
recursive_t = []

for size in input_size:
    # the time taken for iterative distribution
    start = time.time()
    iterativeDistribution(size)
    end = time.time()
    iterative_t.append(end - start)

    # the time taken for recursive distribution
    start = time.time()
    recursiveDistribution(size)
    end = time.time()
    recursive_t.append(end - start)

# plot the graph
plt.figure(figsize=(10, 6))
plt.plot(input_size, iterative_t, label='Iterative Distribution')
plt.plot(input_size, recursive_t, label='Recursive Distribution')
plt.xlabel('Number of Students/Chocolates')
plt.ylabel('Time in seconds')
plt.title('Time Complexity: Iterative vs Recursive Distribution')
plt.legend()
plt.show()


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

# testing the iterative function using the objects above
iterative_dist = iterativeChocDist(choc, students)
print("Iterative Distribution:")
for student, chocolate in iterative_dist: # the distribution of chocolates obtained by each student iteratively
    print(f"{student} gets {chocolate.types}")

# testing the recursive function using the objects above
recursive_dist = recursiveChocDist(choc, students)
print("\nRecursive Distribution:")
for student, chocolate in recursive_dist: # the distribution of chocolates obtained by each student recursively
    print(f"{student} gets {chocolate.types}")

# print the time taken for recursive distribution
print("Time taken for recursive distribution:", timer, "seconds")

#TASK 2
def weightSortChoc(choc): # this function will sort the chocolates by their weight
    start = time.time() # starts timer
    result = sorted(choc, key=lambda x: x.weight) # this line of code will sort the chocolates by weight
    end = time.time() # stops timer
    global timer # access the global timer variable
    timer += end - start # adding the elapsed time to timer
    print("The algorithm took ", end - start, "seconds to sort the chocolates by weight") # time taken to sort the chocolates by weight
    return result # returns the sorted chocolates

def priceSortChoc(choc): # this function will sort the chocolates by their price
    start = time.time() # starts timer
    result = sorted(choc, key=lambda x: x.price) # this line of code will sort the chocolates by price
    end = time.time() # stops timer
    global timer # access the global timer variable
    timer += end - start # adding the elapsed time to timer
    print("The algorithm took ", end - start, " seconds to sort the chocolates by price") # time taken to sort the chocolates by price
    return result # returns the sorted chocolates

# test cases
weightSort = weightSortChoc(choc) # sorts the chocolates by weight and stores the result in weightSort
priceSort = priceSortChoc(choc) # sorts the chocolates by price and stores the result in priceSort

# chocolates sorted by weight
print("\nChocolates sorted by weight:")
for chocolate in weightSort:
    print(f"Type: {chocolate.types}, Weight: {chocolate.weight}")

# chocolates sorted by price
print("\nChocolates sorted by price:")
for chocolate in priceSort:
    print(f"Type: {chocolate.types}, Price: {chocolate.price}")

# printing the time taken for sorting chocolates
print("Time taken for sorting chocolates by weight:", timer, "seconds")



# simulate sorting chocolates by weight
def weightSortChoco(n):
    choc = [Chocolates(weight=i, price=0, types="", ID="") for i in range(n)]
    start = time.time()
    weightSortChoc(choc)
    end = time.time()
    return end - start

# simulate sorting chocolates by price
def priceSortChoco(n):
    choc = [Chocolates(weight=0, price=i, types="", ID="") for i in range(n)]
    start = time.time()
    priceSortChoc(choc)
    end = time.time()
    return end - start

# change the input size and measure the time taken for each sorting method
input = list(range(1, 1001, 100))
weight_sort_times = []
price_sort_times = []

for size in input:
    # Time for sorting chocolates by weight
    weight_sort_times.append(weightSortChoco(size))

    # Time for sorting chocolates by price
    price_sort_times.append(priceSortChoco(size))

# plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(input, weight_sort_times, label='Sorting by Weight')
plt.plot(input, price_sort_times, label='Sorting by Price')
plt.xlabel('Input Size (Number of Chocolates)')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Complexity: Sorting Chocolates')
plt.legend()
plt.show()


#TASK 3
def chocPriceSearch(choc, price): # this function will search for a chocolate by price
    start = time.time() # start recording the time
    for student, chocolate in choc: # for loop to iterate through each chocolate in the list
        if chocolate.price == price: # this will check if the chocolate's price matches the given price
            end = time.time() # ends timer
            global timer # accesses the global timer
            timer += end - start # updates timer with elapsed time
            print("Time taken for searching chocolate by price:", end - start, "seconds")
            return student # return the student who holds the chocolate with the specified price
    end = time.time() # if there is no match the loop will break and stop the timer
    timer += end - start # update timer
    return None # return None if no chocolate with the specified price is found

def chocWeightSearch(choc, weight): # this function will search for a chocolate by weight
    start = time.time() # start recording the time
    for student, chocolate in choc: # for loop to iterate through each chocolate in the list
        if chocolate.weight == weight: # if statement to check if the chocolate's weight matches the specified weight
            end = time.time() # ends timer
            global timer # accesses the global timer
            timer += end - start # updates timer with elapsed time
            print("The algorithm took ", end - start, " seconds to search the chocolate by weight")
            return student # return the student holding the chocolate
    end = time.time() # if there is no match the loop will break and stop the timer
    timer += end - start # update timer
    return None

# Test cases
price = 5
StudentSpecifiedPrice = chocPriceSearch(iterative_dist, price) # search for chocolate by price
if StudentSpecifiedPrice:
    print(f"\nThe student who is holding a chocolate with price {price} is: {StudentSpecifiedPrice}")
else:
    print(f"No student is found holding a chocolate with price {price}")

weight = 9
StudentSpecifiedWeight = chocWeightSearch(iterative_dist, weight) # search for chocolate by weight
if StudentSpecifiedWeight:
    print(f"The student who is holding a chocolate with weight {weight} is: {StudentSpecifiedWeight}")
else:
    print(f"No student is found holding a chocolate with weight {weight}")

# prints the time taken for searching chocolates
print("The algorithm took ", timer, " seconds to search the chocolate by price")

print("\nTotal time:", timer, "seconds")




# simulate searching chocolates by price
def chocoPriceSearch(n):
    chocos = [(None, Chocolates(weight=i, price=i, types="", ID="")) for i in range(n)]
    start = time.time()
    chocPriceSearch(chocos, n - 1)  # search for the highest price
    end = time.time()
    return end - start

# simulate searching chocolates by weight
def chocoWeightSearch(n):
    chocos = [(None, Chocolates(weight=i, price=i, types="", ID="")) for i in range(n)]
    start = time.time()
    chocWeightSearch(chocos, n - 1)  # search for the highest weight
    end = time.time()
    return end - start

# change the input size and measure the time taken for each searching method
input = list(range(1, 1001, 100))
price_search_times = []
weight_search_times = []

for s in input:
    # Time for searching chocolates by price
    price_search_times.append(chocoPriceSearch(s))

    # Time for searching chocolates by weight
    weight_search_times.append(chocoWeightSearch(s))

# graph
plt.figure(figsize=(10, 6))
plt.plot(input, price_search_times, label='Searching by Price')
plt.plot(input, weight_search_times, label='Searching by Weight')
plt.xlabel('Input Size (Number of Chocolates)')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Complexity: Searching Chocolates')
plt.legend()
plt.show()
# Strings
hello_world = "Hello world"
print(hello_world[3])

# List
numbers = [12, 23, 3, 34, -5]
print(numbers[0])

numbers = [1, 2, 3, 4, 5]
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print(doubled_odds)

# Tuplas
tup = (5, 2.0, "Hola")
print(tup[2])

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel['jack'])

# Control structures
# if
x = 3
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(0, 10, 2):
    print(i)

# functions
def sum_range(first, last):
    total = 0
    i = first
    while i <= last:
        total = total + i
        i += 1
    return total

def sum_range_best(first, last):
    return sum(range(first, last+1))


print(sum_range(0, 10))
print(sum_range_best(0, 10))


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        self.__print_trick(trick)

    def get_tricks(self):
        return self.tricks

    def __print_trick(self, trick):
        print(trick)

dog = Dog("Manolo")
dog.add_trick("Jump")


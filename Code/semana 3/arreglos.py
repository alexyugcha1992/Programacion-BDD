import random


numbers = [1,2,3,4,5]
fruits = ["manzana", "pera", "banana"]

new_list = numbers + fruits

numbers[0] = "banana"

# numbers.append(700)
# numbers.insert(3,0)
index = numbers.index(3)
numbers[index] = "change"

print("mi arreglo primero: ", numbers)
numbers.pop()
numbers.remove(2)

print(numbers)

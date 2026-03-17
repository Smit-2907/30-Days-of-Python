# This is the program demostrating some methoda that can be applied on Python List.

numers = [1, 2, 3, 4, 5, 6]
x = numers.copy()
numers.append(7) # Adds an element at the end of the list
print("append():", numers)
numers.insert(1, 69) # Adds an element at the specified position
print("insert():", numers)
numers.remove(2) # Removes the first item with the specified value
print("remove():", numers)
numers.count(6)	# Returns the number of elements with the specified value
print("count()", numers)
numers.pop()	# Removes the element at the specified position
print("pop()", numers)
numers.copy()	# Returns a copy of the list
print("copy(x)", x)
numers.index(5)	# Returns the index of the first element with the specified value
print("index()", numers)

# extend()	Add the elements of a list (or any iterable), to the end of the current list
# reverse()	Reverses the order of the list
# sort()      Sorts the list
# clear()	Removes all the elements from the list
# Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Loop through a set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check if an item exists
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Add an item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add multiple items to a set
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Get the length o a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Remove an item in a set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove an item in a set by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove the last item in a set by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

# Empty a set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Delete a set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists

# Using the set() constructor to create a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.




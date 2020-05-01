# Create List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change the value of a list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if a list item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Get the lengtgh of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add an item to the end of a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Add an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Remove an item at a specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Empty a list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Using the list() constructor to make a list
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change tuple values
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"

# the value is still the same:
print(thistuple[1])

# Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Check if a tuple item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Get the length o tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Delete a tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#this will raise an error because the tuple no longer exists

# Using the tuple() constructor to create a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


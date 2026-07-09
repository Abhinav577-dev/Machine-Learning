# Check whether two lists share common elements (Using Sets)
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

set1 = set(list1)
set2 = set(list2)

if set1.isdisjoint(set2):
    print("The lists share no common elements.")
else:
    print("The lists have common elements.")



# Print duplicate elements in a list (Using Sets)
numbers = list(map(int, input("Enter list elements: ").split()))

seen = set()
duplicate = set()

for num in numbers:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)

print("Duplicate elements:")
print(duplicate)



#Print unique characters and their count
s = input("Enter a string: ")

unique = set(s)

print("Unique characters:")

for ch in unique:
    print(ch)

print("Count of unique characters =", len(unique))
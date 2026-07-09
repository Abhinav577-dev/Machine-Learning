# average of element of list

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total += num

average = total / n

print("Average =", average)


# merging and sorting two lists
n1 = int(input("Enter size of first list: "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second list: "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter element: ")))

result = list1 + list2

result.sort()

print("Merged and Sorted List:")
print(result)
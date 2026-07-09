#Create tuple of even numbers and odd numbers
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = ()
odd = ()

for i in t:
    if i % 2 == 0:
        even = even + (i,)
    else:
        odd = odd + (i,)

print("Even Tuple:", even)
print("Odd Tuple:", odd)
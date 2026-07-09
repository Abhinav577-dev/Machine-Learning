# palindrome of string

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")



# Count spaces in a string
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch == " ":
        count += 1

print("Number of spaces =", count)


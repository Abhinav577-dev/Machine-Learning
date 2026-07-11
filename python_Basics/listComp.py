squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

sq = [i*i for i in range(6) if i%2 != 0]

print(sq)

nums = [-2, -4, 3, -1, 9]
print(nums)
nums = [0 if val<0 else val for val in nums]
print(nums)
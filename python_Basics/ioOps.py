#opening the file using the x mode in which if the file doesnt exists it creates and open for writing
f = open("data.txt", "w+")

f.write("hey hii hello this is the demo  of io operation inn python.\n We are checking the word count along with the line.\n Python is dynamically written language")
f.seek(0)
data = f.read()
print(data)
f.close()


# the different modes of the io operations
# r -> reading default
# w -> writing, overwrites the whole file
# a -> writing, appends at the End
# x -> creates new file & open for writing 
# note -> x throws error if file exists x throws error where w truncates the whole File
# b -> binary Mod
# t -> text mode[default]
# + -> opens disk fie for update (r & w)

with open("sample.txt", "w+") as z:
    z.write("with keyword explanation")
    z.seek(0)
    ans = z.read()
    print(ans)


# using the os module deleting the file
import os 
os.remove("sample.txt")


# word search in the string using the io ops
data = True
line = 1

with open("data.txt", "r") as f:
    while data:
        data = f.readline()
        if("Python" in data):
            print(f"Word found at line no {line}")
            break
        line += 1
local_string = input("Enter string\n")
length = len(local_string)
if length < 255:
    print("{:02x}".format(length+1),end=' ')
    print("{:02d}".format(0),end=' ')

for letter in local_string:
    print(format(ord(letter),"x"),end=' ')
print("{:02d}".format(0))

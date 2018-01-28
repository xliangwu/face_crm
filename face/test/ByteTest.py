import os

buffer = bytes()

data = b'123456'
buffer += data
print(buffer)
print("sub 1:3 ->", buffer[1:3])
print("sub 3 ->", buffer[3:])
print("sub all ->", buffer[:])

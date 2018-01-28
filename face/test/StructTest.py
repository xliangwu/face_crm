from struct import *
from ctypes import create_string_buffer

print(pack('hhl', 1, 2, 3))
print(unpack('!LLLL', b'\x00\x00\xad\xc5\x00\x00\x00\x02\x00\x00\x17\xf2\x00\x00\xad\xb9'))
print(unpack('!L', b'\x77\xab\x77\xab'))
print(pack('!L', 2007725995))
print(unpack('!L', b'w\xabw\xab'))
print(pack('!L', 44485))
print(unpack('!L', b'\x00\x00\xad\xc5'))

str = pack("ii", 20, 1)
print(repr(str))
print(str)

buffer = bytearray(16)
pack_into('!LLLL', buffer, 0, 10, 20, 30, 40)
print(buffer)

unbuffer = unpack_from('!LLLL', buffer, 0)
print(unbuffer)

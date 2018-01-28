import os
import binascii

website = 'http://www.nowcode.cn'
print(type(website))

website_bytes_utf8 = website.encode(encoding="utf-8")
print(type(website_bytes_utf8))
print(website_bytes_utf8)

msgHead = b'\x00\x00\xad\xc5\x00\x00\x00\x02\x00\x00\x17\xf2\x00\x00\xad\xb9'
print(msgHead)

stra = binascii.b2a_hex(msgHead)
print(stra)
print(int(binascii.b2a_hex(b'\x00\x00\xad\xc5'), 16))
print(int(binascii.b2a_hex(b'\x00\x00\x00\x02'), 16))
print(int(binascii.b2a_hex(b'\x00\x00\x17\xf2'), 16))
print(int(binascii.b2a_hex(b'\x00\x00\xad\xb9'), 16))
